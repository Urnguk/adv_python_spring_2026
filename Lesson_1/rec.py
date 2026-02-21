# def func(x):
#     print(x)
#     func(x + 1)


# func(0)

# x = 0
# while True:
#     if x % 10000 == 0:
#         print(x)
#     x += 1

# print(0.1 + 0.2, 0.3)


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_din(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b


print(fib(50))