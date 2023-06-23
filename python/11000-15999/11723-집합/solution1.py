import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        func, num = temp[0], int(temp[1])

        if func == "add":
            S.add(num)
        if func == "remove":
            S.discard(num)
        if func == "check":
            print(1) if num in S else print(0)
        if func == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)