from collections import deque
import sys
input = sys.stdin.readline


def bfs(yaxis, xaxis):
    queue = deque()
    queue.append((yaxis, xaxis))
    graph[yaxis][xaxis] = '1'

    while queue:
        yaxis, xaxis = queue.popleft()
        for dyaxis, dxaxis in dlist:
            Y, X = yaxis + dyaxis, xaxis + dxaxis
            if (0 <= Y < R) and (0 <= X < C) and graph[Y][X] == '#':
                queue.append((Y, X))
                graph[Y][X] = '1'


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

dlist = [(-1, 0), (1, 0), (0, -1), (0, 1)]
count = 0

for i in range(R):
    for j in range(C):
        if graph[i][j] == '#':
            bfs(i, j)
            count += 1

print(count)


# if adjacent # present, goes back to while queue: due to queue.append(X, Y)

# (1) .1....
#     ..#...
#     ..#..#
#     ...##.
#     .#....

# (2) .1....
#     ..1...
#     ..1..#
#     ...##.
#     .#....

# (3) .1....
#     ..1...
#     ..1..1
#     ...##.
#     .#....

# (4) .1....
#     ..1...
#     ..1..1
#     ...1.
#     .#....

# (5) .1....
#     ..1...
#     ..1..1
#     ...11.
#     .1....
