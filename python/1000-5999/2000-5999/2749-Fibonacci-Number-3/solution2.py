num = int(input())
M = num % 1500000
fib_list = [0, 1]

for _ in range(M):
    fib_list.append((fib_list[-1] + fib_list[-2]) % 10**6)

print(fib_list[M])
