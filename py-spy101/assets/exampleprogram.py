import time
import sys

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 10:
        return weirdfib(10)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def weirdfib(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 4:
        return unusualfib(4)
    else:
        return weirdfib(n-1) + weirdfib(n-2)

def unusualfib(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return unusualfib(n-1) + unusualfib(n-2)

def main(num) -> None:
    start_time = time.time()
    result = fibonacci(num)
    end_time = time.time()

    print(f"Fibonacci result: {result}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main(int(sys.argv[1]))