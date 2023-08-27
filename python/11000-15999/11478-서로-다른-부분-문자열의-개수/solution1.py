import sys

input = sys.stdin.readline

S = input().strip()
set_S = set()

for i in range(0, len(S)):
    for j in range(i, len(S)):
        temp = S[i : j + 1]
        if temp in set_S:
            continue
        else:
            set_S.add(temp)

print(len(set_S))
