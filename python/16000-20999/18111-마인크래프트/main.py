import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
blocks = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = sys.maxsize
level = 0

for target in range(257):
    dig, place = 0, 0

    for x in range(N):
        for y in range(M):
            if blocks[x][y] > target:
                dig += blocks[x][y] - target
            else:
                place += target - blocks[x][y]
        
    if dig + B >= place:
        if place + (dig * 2) <= answer:
            answer = place + (dig * 2)
            level = target

print(answer, level)