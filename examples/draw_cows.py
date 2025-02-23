"""
Example 1: draw a herd of cows, using `llm_complete`.
"""
from jit_completion import llm_complete

@llm_complete()
def draw_cows(nums : int) -> str:
    """
    Draw a bunch of cows that looks like what you get from cowsay as ASCII art.
    Args:
    - nums (int): specify how many cows should stand side-by-side. 
    """
    many_cows = 'lots of cows, please implement'
    # Cows stand side by side. 
    # Pay attention to spaces and padding!
    # Remember to ADD PADDING to each line of the cow ASCII art, 
    # so that len(line) for each line is equal! Otherwise it looks wrong!
    return many_cows

# Calls
print(draw_cows(2))
print('\n-----------')
code = getattr(draw_cows, 'raw')
print(f"Function is defined as below:\n```python\n{code}\n```")
#  ^__^              ^__^              ^__^              ^__^              ^__^              ^__^             
#  (oo)\_______      (oo)\_______      (oo)\_______      (oo)\_______      (oo)\_______      (oo)\_______     
#  (__)\       )\/\  (__)\       )\/\  (__)\       )\/\  (__)\       )\/\  (__)\       )\/\  (__)\       )\/\ 
#      ||----w |         ||----w |         ||----w |         ||----w |         ||----w |         ||----w |    
#      ||     ||         ||     ||         ||     ||         ||     ||         ||     ||         ||     ||    
#
# To be fair, this isn't very stable. You can try running it several times and see what happens
