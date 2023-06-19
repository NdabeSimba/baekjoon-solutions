import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
result = []

for _ in range(N):
    board.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        black_board = 0
        white_board = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != "B":
                        black_board += 1
                    if board[a][b] != "W":
                        white_board += 1
                else:
                    if board[a][b] != "W":
                        black_board += 1
                    if board[a][b] != "B":
                        white_board += 1

        result.append(black_board)
        result.append(white_board)

print(min(result))