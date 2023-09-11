import sys
from collections import deque


input = sys.stdin.readline
num = int(input())
deq = deque()

for _ in range(num):
    inp = list(map(int, input().split()))

    if inp[0] == 1:
        deq.appendleft(inp[1])

    elif inp[0] == 2:
        deq.append(inp[1])

    elif inp[0] == 3:
        if deq:
            print(deq.popleft())
        else:
            print(-1)

    elif inp[0] == 4:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    
    elif inp[0] == 5:
        print(len(deq))

    elif inp[0] == 6:
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    
    elif inp[0] == 7:
        if deq:
            print(deq[0])
        else:
            print(-1)
    
    elif inp[0] == 8:
        if deq:
            print(deq[-1])
        else:
            print(-1)