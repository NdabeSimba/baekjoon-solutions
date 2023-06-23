import sys

N = int(input())
S = [0 for _ in range(21)]

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "add":
        S[int(command[1])] = 1

    if command[0] == "remove":
        S[int(command[1])] = 0

    if command[0] == "check":
        if S[int(command[1])] == 1:
            print(1)
        else:
            print(0)

    if command[0] == "toggle":
        if S[int(command[1])] == 0:
            S[int(command[1])] = 1
        else:
            S[int(command[1])] = 0

    if command[0] == "all":
        S = [1 for _ in range(21)]

    if command[0] == "empty":
        S = [0 for _ in range(21)]