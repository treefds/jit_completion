"""
Default prompts for JIT Completion.
"""

PROMPT_JIT_COMPLETION_THINK = """\
You are an expert programmer, tasked with completing the implementation of a Python function. 
You will be given an incomplete Python function definition. You must infer the purpose and expected implementation based on the provided code, and return a executeable implementation of the function. 

## REQUIREMENTS
- You must NOT change the function name. You must NOT change the existing function annotations, docstrings and return statement (if available).
- Your function MUST be executeable.
- If you believe there is not enough information about the function, you should nevertheless try to return a working function.
- You should think before you code. Put your thinking process after `### THINK`, and put the code after `### CODE`.

The input and output format, as well as examples are specified below.

## INPUT FORMAT

```python
# The function that should be completed.
def example_function(x):
    # calculate y as the power of x.
    y : int = NotImplemented
    return y
```
    
## OUTPUT FORMAT
### THINK
(Your thinking process in natural language...)

### CODE
```python
# Your implementation of the function.
def example_function(x):
    y = x * x
    return y
```

Given below is the user input. Output code based on the following input.

## INPUT
```python
{code}
```
"""

PROMPT_JIT_COMPLETION = """\
You are an expert programmer, tasked with completing the implementation of a Python function. 
You will be given an incomplete Python function definition. You must infer the purpose and expected implementation based on the provided code, and return a executeable implementation of the function. 

## REQUIREMENTS
- You must NOT change the function name. You must NOT change the existing function annotations, docstrings and return statement (if available).
- Your function MUST be executeable.
- You should always try to return a working function.

The input and output format, as well as examples are specified below.

## INPUT FORMAT

```python
# The function that should be completed.
def example_function(x):
    # calculate y as the power of x.
    y : int = NotImplemented
    return y
```
    
## OUTPUT FORMAT

```python
# Your implementation of the function.
def example_function(x):
    y = x * x
    return y
```

Given below is the user input. Output code based on the following input.

## INPUT
```python
{code}
```
"""

PROMPT_JIT_MOCK = """\
You are mimicking a Python API. The API function's name is `{name}`. Given the function's annotations and descriptions, you should mimick the function's outputs.

### ANNOTATIONS
{annotations}

### ARGS
{func_args}

### KWARGS
{func_kwargs}

### INSTRUCTIONS
{docstring}

NOTES: Your output should be interpretable with Python `eval()` function, and matches the types given in 'return' annotation (if available). 
Do NOT output anything other than text results that is directly interpretable with `eval`. 
Do NOT use any Markdown formatting. Markdown syntax like "```python" is strictly prohibited.
Be especially careful with formatting and especially quotation marks.
"""