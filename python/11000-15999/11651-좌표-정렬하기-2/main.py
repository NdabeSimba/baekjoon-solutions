import sys
input = sys.stdin.readline

N = int(input())
lis = [list(map(int, input().split())) for _ in range(N)]

lis.sort(key=lambda x : (x[1], x[0]))

for l in lis:
    print(*l)