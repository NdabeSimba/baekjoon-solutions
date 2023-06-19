import sys

input = sys.stdin.readline

num_class = int(input())

for _ in range(num_class):
    num = list(map(int, input().split()))
    sum = 0
    ave_num = 0
    for i in range(1, num[0] + 1):
        sum += num[i]
        ave = sum / num[0]
    for j in range(1, num[0] + 1):
        if num[j] > ave:
            ave_num += 1
    count = ave_num / num[0] * 100
    print(f"{count:.3f}%")
