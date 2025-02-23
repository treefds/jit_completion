"""
Implements time decorator
"""
from jit_completion import llm_complete, llm_mock
import time

@llm_complete()
def timer(func):
    """
    Decorator for timing functions.
    Modifies the output of decorated function to (execution_time, output1, output2, ...)
    where `execution_time` is the time needed to execute this function.
    """
    def wrapper(*args, **kwargs):
        return ...
    return wrapper

@timer
@llm_mock()     # llm_mock() must come last or else it would break
def make_a_joke(topic : str) -> str:
    """
    Tell a joke about the given the topic.
    """
    return "insert a joke"

if __name__ == "__main__":
    execution_time, joke = make_a_joke("Birch trees")
    print(f"Execution time: {execution_time}\nJoke: {joke}")
