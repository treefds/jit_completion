"""
JIT Completion decorator implementations.
"""
import re
import inspect
from typing import Callable
from functools import wraps
import openai
from .prompts import PROMPT_JIT_COMPLETION, PROMPT_JIT_MOCK

def llm_complete(
        *,
        client=None,
        model : str = 'gpt-4o',
        prompt_template : str = PROMPT_JIT_COMPLETION
    ):
    """
    Decorator generator for JIT LLM auto-completion of functions.

    Uses OpenAI library for LLM calls.

    Usage:
    ```python
    @llm_complete()
    def func():
        ...
    ```

    Args:
    - model (str): LLM model name.
    - prompt_template (str): The user prompt template. Must contains `{code}`.
    """
    if not isinstance(model, str):
        raise ValueError('"model" is not a str')
    if not isinstance(prompt_template, str):
        raise ValueError('"prompt_template" is not a valid str')
    if not prompt_template:
        raise ValueError('"prompt_template" is not a valid str')
    if '{code}' not in prompt_template:
        raise ValueError('"Bad format: prompt_template" does not contain `{code}`')

    def decorator(func : Callable):
        try:
            old_code = inspect.getsource(func)
            caller_frame = inspect.currentframe().f_back
        except Exception as exception:
            raise RuntimeError("Unable to get function definition.") from exception

        assert old_code, "The inspected function is empty or invalid"
        assert 'def' in old_code, "Cannot find `def` in function"
        old_code = old_code[old_code.find("def "):]

        user_message = prompt_template.format(code=old_code)
        response = call_llm(model, user_message, client)
        new_codes = re.findall(r"```python\n(.*)\n```", response, re.DOTALL)
        if not new_codes:
            raise RuntimeError("Cannot find any matching regex in LLM response.")
        new_code = new_codes[0]

        exec(new_code, caller_frame.f_globals, caller_frame.f_locals)
        new_func = caller_frame.f_locals.get(func.__name__)
        if not new_func:
            raise RuntimeError(f"Failed to define new function `{func.__name__}`!")
        setattr(new_func, 'raw', new_code)

        return new_func
    return decorator


def llm_mock(*, client=None, model : str = 'gpt-4o', prompt_template : str = PROMPT_JIT_MOCK):
    """
    Decorator generator for JIT LLM auto-mocking for functions.

    Uses OpenAI library for LLM calls.

    Usage:
    ```python
    @llm_mock()
    def func():
        ...
    ```

    Args:
    - model (str): LLM model name.
    - prompt_template (str): The user prompt template.\
      Contains {name}, {annotations}, {docstrings}, {func_args}, {func_kwargs}.
    """
    if not isinstance(model, str):
        raise ValueError('"model" is not a str')
    if not isinstance(prompt_template, str):
        raise ValueError('"prompt_template" is not a valid str')
    if not prompt_template:
        raise ValueError('"prompt_template" is not a valid str')

    def decorator(func : Callable):
        signature = inspect.signature(func)
        default_kwargs = {
            kw: value.default
                for kw, value in signature.parameters.items()
                if value.default != inspect.Signature.empty
        }
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_message = prompt_template.format(
                name=func.__name__,
                annotations=func.__annotations__,
                docstring=func.__doc__,
                func_args=args,
                func_kwargs=default_kwargs | kwargs
            )
            response = call_llm(model, user_message, client)
            try:
                result = eval(response)
            except Exception as exception:
                raise RuntimeError("LLM call evaluation failed") from exception
            return result
        return wrapper
    return decorator


def call_llm(model : str, message : str, client : openai.OpenAI = None):
    """
    Call LLM using OpenAI API.

    Args:
    - model (str): model name.
    - message (str): user message.
    """
    messages = [{"role": "user", "content": message}]
    completions = \
        client.chat.completions if isinstance(client, openai.OpenAI) else openai.chat.completions
    response = completions.create(
        model=model,
        messages=messages
    )
    response_text = response.choices[0].message.content
    return response_text
