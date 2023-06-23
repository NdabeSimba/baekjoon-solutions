import sys
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    if x >= M or x < 0 or y >= N or y < 0:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            DFS(x + dx[i], y + dy[i])
        return True
    
    return False

answer = []

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if DFS(i, j):
                count += 1

    print(count)