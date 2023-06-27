import sys
input = sys.stdin.readline

def fib(n):
    num_list = [1, 2, 4]
    if n < 4:
        return num_list[n - 1]
    else:
        for i in range(3, n):
            num_list.append(num_list[i - 1] + num_list[i - 2] + num_list[i - 3])
        return num_list[-1]


N = int(input())

for _ in range(N):
    num = int(input().strip())
    print(fib(num))