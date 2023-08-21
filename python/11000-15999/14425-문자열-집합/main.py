import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S_set = set()
string_list = list()
result = 0

for _ in range(N):
    S_set.add(input().strip())

for _ in range(M):
    string_list.append(input().strip())

for i in range(M):
    temp = string_list.pop()
    if temp in S_set:
        result += 1
    else:
        continue

print(result)