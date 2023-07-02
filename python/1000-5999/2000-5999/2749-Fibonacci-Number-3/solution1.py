input = __import__("sys").stdin.readline
num = int(input())

M = num % 1500000
num1, num2 = 0, 1

for _ in range(M):
    num1, num2 = num2, (num1 + num2) % 1000000

print(num1)
