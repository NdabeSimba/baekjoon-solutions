def fib(n):
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    
    return b
    
n = int(input())
print(fib(n), n - 2)