import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def factorial(n):
    result = 1
    if n == 0 or n == 1:
        return result
    else:
        for i in range(1,n+1):
            result *= i
        return result

print(factorial(N) // (factorial(N-K) * factorial(K)))