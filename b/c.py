def fib(n, a=1, b=1):
    for _ in range(n):
        a, b = b, a + b
    return a

"add ddd"
