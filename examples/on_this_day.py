"""
Example 3: Tell what happened today in history, using llm_mock.
"""
import time
from jit_completion import llm_mock

@llm_mock()
def on_this_day(date : str) -> str:
    """
    Return one (and only one) short description of a random historical event that happened on this date.
    """
    return "A random incident from the history"

print(on_this_day("March 14th"))
print(on_this_day(time.strftime("%m-%d")))
# On March 14th, 1879, Albert Einstein, the renowned physicist known for the theory of relativity, was born in Ulm, Germany.
# On February 23, 1945, during World War II, U.S. Marines raised the American flag on Iwo Jima's Mount Suribachi.
