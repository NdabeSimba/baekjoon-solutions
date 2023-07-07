# input = __import__("sys").stdin.readline
num = input()
num1 = " ".join(num.split("0")).split()
num2 = " ".join(num.split("1")).split()
count = 0
print(min(len(num1), len(num2)))
