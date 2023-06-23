import sys
input = sys.stdin.readline

M = int(input())
S = set()
S_all = set([str(i) for i in range(1, 21)])

for _ in range(M):
    cmd = list(input().split())

    if cmd[0] == "all":
        S = S_all

    if cmd[0] == "empty":
        S = set()

    if cmd[0] == "add":
        S.add(cmd[1])

    if cmd[0] == "remove":
        S.discard(cmd[1])

    if cmd[0] == "check":
        sys.stdout.write("1\n" if cmd[1] in S else "0\n")

    if cmd[0] == "toggle":
        if cmd[1] in S: 
            S.discard(cmd[1])
        else: 
            S.add(cmd[1])