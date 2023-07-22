import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

num_list = list()


def decimal(n):
    if n == 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True


for num in range(M, N + 1):
    if decimal(num):
        num_list.append(num)

if len(num_list) > 0:
    print(sum(num_list))
    print(min(num_list))
else:
    print(-1)
