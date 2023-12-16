import sys

input = sys.stdin.readline

N = int(input())
count = 0

while N % 2 != 0 and N % 3 != 0:
    N = N - 1
    count += 1

while N % 2 == 0 or N % 3 == 0:
    if N % 3 == 0:
        N = N / 3
        count += 1
    else:
        N = N / 2
        count += 1

print(count)