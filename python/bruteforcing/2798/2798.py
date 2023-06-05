# solution using 3 for loops

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i + 1, N):
        for z in range(j + 1, N):
            card_sum = card_list[i] + card_list[j] + card_list[z]
            if card_sum <= M:
                result = max(result, card_sum)    
print(result)


# solution using permutations

from itertools import permutations

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
num_list = []

for three in permutations(card_list, 3):
    if sum(three) > M:
        continue
    else:
        num_list.append(sum(three))
print(max(num_list))


# solution using combinations

from itertools import combinations

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
num_list = []

for three in combinations(card_list, 3):
    if sum(three) > M:
        continue
    else:
        num_list.append(sum(three))
print(max(num_list))