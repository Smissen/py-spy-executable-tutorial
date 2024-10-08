import time

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 10:
        return fibono(10)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibono(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 4:
        return fib4(4)
    else:
        return fibono(n-1) + fibono(n-2)

def fib4(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib4(n-1) + fib4(n-2)

def main() -> None:
    start_time = time.time()
    result = fibonacci(35)
    end_time = time.time()

    print(f"Fibonacci result: {result}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()