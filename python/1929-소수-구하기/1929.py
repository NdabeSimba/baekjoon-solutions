# time exceeded
import sys

input = sys.stdin.readline

num = list(map(int, input().split()))
prime = []

for h in range(num[0], num[1]):
    for i in range(h):
        no = 0
        if h > 1:
            for j in range(2, h):
                if h % j == 0:
                    no += 1
            if no == 0:
                prime.append(h)

print(*set(prime), sep="\n")


# sieve of eratosthenes algorithm
# time complexity O(N^(1/2))
M, N = map(int, input().split())

for i in range(M, N + 1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)


# function solution
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True


M, N = map(int, input().split())

for i in range(M, N + 1):
    if isPrime(i):
        print(i)
