num = input()
num1 = list(filter(None, num.split("0")))
num2 = list(filter(None, num.split("1")))
count = 0
print(min(len(num1), len(num2)))
