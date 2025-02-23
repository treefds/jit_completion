"""
Example 2: Draw a fish based on its age.
"""
from jit_completion import llm_complete

class Fish:
    def __init__(self, age):
        self.age = age
    
    @property
    @llm_complete()      # Must come last, or else it would break
    def appearance(self) -> str:
        """
        Returns an ASCII art of the appearance of a fish, based on `self.age` (float).
        The length of the fish is related to its age.
        As the fish gets older, it would stop growing. 
        Fish dies at 15yo. Dead fish has `X` eyes.
        """
        # Base the Fish on this: <•))))><
        return str('the fish')

if __name__ == "__main__":
    for i in range(1, 16):
        print(i, Fish(i).appearance)

# 1 <•)><
# 2 <•))><
# 3 <•)))><
# 4 <•))))><
# 5 <•)))))><
# 6 <•))))))><
# 7 <•)))))))><
# 8 <•))))))))><
# 9 <•)))))))))><
# 10 <•))))))))))><
# 11 <•))))))))))><
# 12 <•))))))))))><
# 13 <•))))))))))><
# 14 <•))))))))))><
# 15 <X))))><
