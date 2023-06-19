import sys
input = sys.stdin.readline


def dfs(x, y):

    if graph[x][y] == '-':
        graph[x][y] = 1
        for dy in [1, -1]:  # check right/left
            Y = y + dy
            if (Y > 0 and Y < M) and graph[x][Y] == '-':
                dfs(x, Y)

    if graph[x][y] == '|':
        graph[x][y] = 1
        for dx in [1, -1]:  # check up/down
            X = x + dx
            if (X > 0 and X < N) and graph[X][y] == '|':
                dfs(X, y)


N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i, j)
            count += 1

print(count)
