import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    if x <= -1 or x >= N or y <= -1 or y > M:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0

        for i in range(4):
            DFS(x + dx[i], y + dy[i])
        
        return True
    return False

answer = []
for _ in range(T):
    M, N, K = list(map(int, input().split()))

    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
