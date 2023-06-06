import sys

input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
comp = list(map(int, input().split()))


count = {}
for i in cards:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in comp:
    if i in count:
        print(count[i], end=' ')
    else:
        print(0, end=' ')