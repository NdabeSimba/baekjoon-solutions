input = __import__("sys").stdin.readline
num = int(input())


def fib(n):
    num1, num2 = 0, 1
    if n == 0:
        return num1

    for _ in range(n - 1):
        num1, num2 = num2, num1 + num2

    return num2


print(fib(num))