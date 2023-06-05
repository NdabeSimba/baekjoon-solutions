import sys

input = sys.stdin.readline

num = int(input())
lis = map(int, input().split())
prime = 0

for i in lis:
    no = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                no += 1
        if no == 0:
            prime += 1

print(prime)
