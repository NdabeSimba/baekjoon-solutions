import sys
input = sys.stdin.readline

n, l = map(int,input().split())
fruit = list(map(int,input().split()))
fruit.sort()

for i in range(n):
    if fruit[i] <= l:
        l += 1
    else:
        break
print(l)