from itertools import combinations

input = __import__('sys').stdin.readline
N = int(input())

dec = set()

for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(map(str, reversed(j)))
        dec.add(int(num))

dec = sorted(dec)

if N < len(dec): print(dec[N])
else: print(-1)