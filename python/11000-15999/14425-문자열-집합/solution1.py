import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S_set = set()
result = 0

for _ in range(N):
    S_set.add(input().strip())

for i in range(M):
    temp = input().strip()
    if temp in S_set:
        result += 1
    else:
        continue

print(result)