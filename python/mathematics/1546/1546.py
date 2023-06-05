import sys
input = sys.stdin.readline

num = int(input())
lis = list(map(int,input().split()))
max_num = sorted(lis)[-1]
sum = 0

for i in range(num):
    lis[i] = lis[i]/max_num*100
    sum += lis[i]

print(sum/num)