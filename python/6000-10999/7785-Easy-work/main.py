import sys
input = sys.stdin.readline

N = int(input())
indoor_set = set()

for _ in range(N):
    a, b = list(input().strip().split())

    if b == "enter":
        indoor_set.add(a)
    else:
        indoor_set.discard(a)

in_list = sorted(indoor_set, reverse=True)

print(*in_list, sep="\n")