input = __import__('sys').stdin.readline

N = int(input())
C = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(C):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
count = 0
visited = [False] * (N + 1)


def DFS(n):
    global count
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            DFS(i)
            count += 1

DFS(1)
print(count)