import sys

input = sys.stdin.readline
N = int(input())
comp = []

for i in range(N):
    comp.append(list(map(int, input().split())))

result = sorted(comp, key=lambda x: (x[0], x[1]))

for out in result:
    print(*out,end="\n")
