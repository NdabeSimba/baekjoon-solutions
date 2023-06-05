import sys
input = sys.stdin.readline

num = int(input())
num_list = sorted(list(map(int, input().split())))
num_sum = 0
result = 0

for i in range(num):
    num_sum += num_list[i]
    result += num_sum
print(result)