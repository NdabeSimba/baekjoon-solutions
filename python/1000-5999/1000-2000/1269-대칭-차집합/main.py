import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = 0
result += len(A - B)
result += len(B - A)

print(result)