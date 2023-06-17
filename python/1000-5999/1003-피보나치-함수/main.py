import sys
input = sys.stdin.readline

count0 = [1, 0, 1]
count1 = [0, 1, 1]

def fibonacci(n):
    length = len(count0)
    if n >= length:
        for i in range(length, n+1):
            count0.append(count0[i-1] + count0[i-2])
            count1.append(count1[i-1] + count1[i-2])
    
    return count0[n], count1[n]

T = int(input())

for _ in range(T):
    print(*fibonacci(int(input())))
