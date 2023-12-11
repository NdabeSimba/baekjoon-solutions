import sys

input = sys.stdin.readline

N, M = map(int, input().split())
Nlist = list(map(int, input().split()))

for i in range(N - 1):
    Nlist[i + 1] += Nlist[i]

Nlist.insert(0, 0)

for _ in range(M):
    a, b = map(int, input().split())
    print(Nlist[b] - Nlist[a - 1])
