import itertools

N, M = map(int, input().split())

arr = [i + 1 for i in range(N)]
nCr = itertools.combinations(arr, M)

for i in nCr:
    print(*i)
