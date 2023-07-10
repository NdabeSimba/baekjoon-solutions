input = __import__("sys").stdin.readline
stick_list = [64, 32, 16, 8, 4, 2, 1]
count = 0

X = int(input())

for stick in stick_list:
    if X >= stick:
        X -= stick
        count += 1
    
    if X == 0:
        break

print(count)