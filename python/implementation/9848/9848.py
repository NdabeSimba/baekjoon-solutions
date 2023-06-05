import sys
input = sys.stdin.readline

num, com = map(int,input().split())
gift = 0
lis = list(int(input()) for i in range(num))
for i in range(0,num-1):
    if lis[i] - lis[i+1] >= com:
        gift +=1
    else:
        pass
print(gift)