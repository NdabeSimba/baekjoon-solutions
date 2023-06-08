import sys

input = sys.stdin.readline

M = int(input())
cup = [1, 2, 3]

for _ in range(M):
    X, Y = map(int, input().split())
    cup[X - 1], cup[Y - 1] = cup[Y - 1], cup[X - 1]

print(cup.index(1) + 1)
