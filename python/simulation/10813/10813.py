import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ball_lis = []
ball_take = 0

for i in range(1,N+1):
    ball_lis.append(i)
for _ in range(M):
    i, j = map(int, input().split())
    ball_take = ball_lis[i-1]
    ball_lis[i-1] = ball_lis[j-1]
    ball_lis[j-1] = ball_take
print(*ball_lis)