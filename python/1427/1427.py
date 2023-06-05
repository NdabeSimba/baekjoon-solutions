import sys
input = sys.stdin.readline
num = list(input())
num = sorted(num, reverse = True)
print(''.join(num))