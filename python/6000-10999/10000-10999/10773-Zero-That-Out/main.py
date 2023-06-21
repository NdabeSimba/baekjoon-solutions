import sys
input = sys.stdin.readline
K = int(input())
num_lis = []

for _ in range(K):
    num = int(input())
    if num == 0:
        num_lis.pop()
    else:
        num_lis.append(num)
    
print(sum(num_lis))