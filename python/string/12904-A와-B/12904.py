import sys
input = sys.stdin.readline

S = list(str(input().strip()))
T = list(str(input().strip()))

while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1] 
        # list[<start>:<stop>:<step>]
    print(T)

if S == T:
    print(1)
else:
    print(0)