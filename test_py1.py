N = int(input())

def factorial(n):
    if n <= 1:
        return n
    else:
        return factorial(n - 1) + factorial(n - 2)
    
print(factorial(N))