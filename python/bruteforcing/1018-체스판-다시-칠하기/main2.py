""" 
result: 31
8 8
BBBBBBBB
BBBBBBBB
BBBBBBBB
BBBBBBBB
BBBBBBBB
BBBBBBBB
BBBBBBBB
BBBBBBBB
"""

def get_count(i, j):
    cnt_w, cnt_b = 0, 0

    for a in range(i, i + 8):
        for b in range(j, j + 8):
            if case_w[a][b]:
                cnt_w += 1
            if case_b[a][b]:
                cnt_b += 1
    return min(cnt_w, cnt_b)

if __name__ == "__main__":
    # 입력
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    case_w = [[False for _ in range(M)] for _ in range(N)]
    for i, row in enumerate(board):
        now = 'W' if i % 2 == 0 else 'B'
        for j, col in enumerate(row):
            if now != col:
                case_w[i][j] = True
            now = 'W' if now == 'B' else 'B'
    print(case_w)

    case_b = [[False for _ in range(M)] for _ in range(N)]
    for i, row in enumerate(board):
        now = 'B' if i % 2 == 0 else 'W'
        for j, col in enumerate(row):
            if now != col:
                case_b[i][j] = True
            now = 'W' if now == 'B' else 'B'
    print(case_b)

    answer = N * M
    for i in range(N - 7):
        for j in range(M - 7):
            answer = min(answer, get_count(i, j))

    # 출력
    print(answer)
