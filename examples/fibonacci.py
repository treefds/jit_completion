from jit_completion import llm_complete

@llm_complete()
def fibonacci(x : int) -> int:
    """
    Recursively get the x-th number from fibonacci sequence f,
    where f[0] = 0; f[1] = 1.
    """
    return int()

if __name__ == "__main__":
    print(f"fibonacci(10) = {fibonacci(10)}")
    print("-----------------------")
    print(fibonacci.raw)