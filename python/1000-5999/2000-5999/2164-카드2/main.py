from collections import deque


N = deque([i + 1 for i in range(int(input()))])

while len(N) > 1:
    N.popleft()
    temp = N.popleft()
    N.append(temp)

print(N[0])

def f(n):
    if n<=2:
        return n
    else:
        if n%2==0:
            return 2*f(n//2)
        if n%2==1:
            return 2*f((n+1)//2)-2
print(f(int(input())))