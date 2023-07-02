# pisano period
# Fibonacci numbers modulo 3 begins:
# 0, 1, 1, 2, 0, 2, 2, 1, 0, 1, 1, 2, 0, 2, 2, 1, 0, 1, 1, 2, 0, 2, 2, 1, 0, ...

input = __import__("sys").stdin.readline

M = 1000000
Per = 1500000

num = int(input())


def fib(n):
    num1, num2 = 0, 1

    for _ in range(n):
        num1, num2 = num2 % M, (num1 + num2) % M

    return num1


print(fib(num % Per))
