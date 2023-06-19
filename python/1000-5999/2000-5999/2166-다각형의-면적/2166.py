import sys
input = sys.stdin.readline

num = int(input())
sum = 0

lis = [list(map(int, input().split())) for _ in range(num)]
lis.append(lis[0])

for i in range(num):
    sum += (lis[i][0] * lis[i+1][1]) - (lis[i][1] * lis[i+1][0])

print(round(abs(sum/2), 1))
