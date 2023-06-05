import sys

input = sys.stdin.readline

num = int(input())
num_lis = []

for _ in range(num):
    num_lis.append(int(input()))

count = 0
max = 0

for i in reversed(num_lis):
    if max < i:
        max = i
        count += 1
print(count)
