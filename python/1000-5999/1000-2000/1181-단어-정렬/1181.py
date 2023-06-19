# num = int(input())
# lis = []

# for _ in range(num):
#     lis.append(input())

# lis = list(set(lis))
# lis.sort()
# lis.sort(key = len)

# print(*lis,sep="\n")

# memory 35868 KB, time 820 ms

import sys
input = sys.stdin.readline

num = int(input())
lis = []

for _ in range(num):
    lis.append(input().strip())

lis = list(set(lis))
lis.sort()
lis.sort(key = len)

print(*lis,sep="\n")

# memory 35868 KB, time 72 ms