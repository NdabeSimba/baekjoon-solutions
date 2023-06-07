import sys
input = sys.stdin.readline

N, K = map(int, input().split())

idx = 0
queue = [i for i in range(1, N + 1)]
result = []

while queue:
    idx += K - 1
    if idx >= len(queue): 
        idx %= len(queue)
    result.append(str(queue.pop(idx)))

print('<',end='')
print(*result, sep=', ', end='')
print('>')