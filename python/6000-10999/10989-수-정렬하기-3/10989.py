import sys
input = sys.stdin.readline

# lis = []
# num = int(input())
# for _ in range(num):
#     lis.append(int(input()))
# lis = sorted(lis)
# for i in range(num):
#     print(lis[i])

# memory limit exceeded

num = int(input())
lis = [0]*10001
for _ in range(num):
    lis[int(input())] += 1

for i in range(10001):
    if lis[i] != 0:
        for j in range(lis[i]):
            print(i)
# counting sort, time complexity = O(n)