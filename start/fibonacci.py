def print_fibonacci(count: int):
    for x in range(count):
        print(fib(x))


def fib(n: int):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


print_fibonacci(10)
