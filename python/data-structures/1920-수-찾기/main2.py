N = int(input())
num_lis = set(map(int, input().split()))
M = int(input())
compare = list(map(int, input().split()))

for i in compare:
    print(1) if i in num_lis else print(0)