input = __import__("sys").stdin.readline
num = list(map(int, input().strip()))
count = 0

for i in range(len(num) - 1):
    if num[i] != num[i + 1]:
        count += 1

print((count + 1) // 2)
