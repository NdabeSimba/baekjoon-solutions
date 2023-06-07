from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

que = deque(i + 1 for i in range(N))
result = []

while que:
    for _ in range(K - 1):
        que.append(que.popleft())
    result.append(que.popleft())

print("<", ", ".join(result), ">", sep="")
