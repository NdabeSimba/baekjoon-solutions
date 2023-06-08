# 3836 ms

# num = int(input())
# card = {
#     'STRAWBERRY': 0,
#     'BANANA': 0,
#     'LIME': 0,
#     'PLUM': 0
# }

# for _ in range(num):
#     fruit, count = input().split()
#     card[fruit] += int(count)

# if 5 in card.values():
#     print("YES")
# else:
#     print("NO")

# 108 ms

import sys
input = sys.stdin.readline

num = int(input())
card = {
    'STRAWBERRY': 0,
    'BANANA': 0,
    'LIME': 0,
    'PLUM': 0
}

for _ in range(num):
    fruit, count = input().split()
    card[fruit] += int(count)

if 5 in card.values():
    print("YES")
else:
    print("NO")
