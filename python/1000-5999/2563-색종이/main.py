import sys
input = sys.stdin.readline

N = int(input())
grid = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            grid[i][j] = 1

answer = 0

for point in grid:
    answer += point.count(1)

print(answer)