import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = set()
seen = set()
result = set()

for _ in range(N):
    listen.add(input().strip())

for _ in range(M):
    seen.add(input().strip())

result = listen & seen

print(len(result), *sorted(result), sep="\n")