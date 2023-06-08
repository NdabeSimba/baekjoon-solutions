import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    H, W, N = map(int,input().split())
    room_num = N // H + 1
    floor = N % H

    if N % H == 0:
        room_num = N // H
        floor = H

    print(f'{floor * 100 + room_num}')