import sys
input = sys.stdin.readline

num = int(input())

for i in range(1,num):
    print(" "*(num-i) + "*"*(i*2-1))

for j in range(num, 0, -1):
    print(" "*(num-j) + "*"*(j*2-1))