import sys

input = sys.stdin.readline

A, B = map(int, input().split())
A, B = max(A, B), min(A, B)
result = A * B

while B != 0:
    A, B = B, A % B

print(result // A)
