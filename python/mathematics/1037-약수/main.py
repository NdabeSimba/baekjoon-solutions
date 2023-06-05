# 1
N = int(input())
num = sorted(list(map(int, input().split())))

if N == 1:
    print(num[0] * num[0])
else:
    print(num[0] * num[-1])

# 2
N = int(input())
lis = list(map(int, input().split()))
print(max(lis) * min(lis))
