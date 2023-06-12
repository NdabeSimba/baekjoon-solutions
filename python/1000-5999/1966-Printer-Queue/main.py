from collections import deque
import sys
input = sys.stdin.readline

t_case = int(input())

for _ in range(t_case):
    n, m = map(int, input().split())
    prior = deque(list(map(int, input().split())))
    count = 0

    while prior:
        pri = max(prior)
        front = prior.popleft()
        m -= 1
        if pri == front:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            prior.append(front)
            if m < 0:
                m = len(prior) - 1