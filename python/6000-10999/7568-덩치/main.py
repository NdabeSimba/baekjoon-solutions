import sys
input = sys.stdin.readline

N = int(input())

lis = [list(map(int, input().split())) for _ in range(N)]

for point in lis:
    rank = 1
    
    for compare in lis:
        if point[0] < compare[0] and point[1] < compare[1]:
            rank += 1

    print(rank, end=' ')
