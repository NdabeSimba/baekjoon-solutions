from sys import stdin


def wrongs_finder(y, x):
    if y != n-1 and check_wrongs[y+1][x] == -1: #when the point is not at the downside of the board and it is not checked yet
        if chessboard[y][x] == chessboard[y+1][x]: #when the point and point below are the same
            chessboard[y+1][x] = 1 - chessboard[y][x]
            check_wrongs[y+1][x] = 1
        else: #when the point and point below are not the same
            check_wrongs[y+1][x] = 0
        wrongs_finder(y+1, x)

    if x != m-1 and check_wrongs[y][x+1] == -1: #when the point is not at the rightside of the board and it is not checked yet
        if chessboard[y][x] == chessboard[y][x+1]:
            chessboard[y][x+1] = 1 - chessboard[y][x]
            check_wrongs[y][x+1] = 1
        else:
            check_wrongs[y][x+1] = 0
        wrongs_finder(y, x+1)

n, m = map(int, stdin.readline().split())

chessboard = [[] for _ in range(n)] #1 is White, 0 is black (int)
correct_placement = [[] for _ in range(n)] #0 is correct, 1 is wrong
check_wrongs = [[-1 for __ in range(m)] for _ in range(n)] #list for checking the wrongs in 8X8 board, 1 is wrong, 0 is right, -1 is not checked


for i in range(n):
    line = stdin.readline().split()[0]
    for piece in line:
        if piece == 'W': chessboard[i].append(1)
        else: chessboard[i].append(0)

check_wrongs[0][0] = 0
wrongs_finder(0, 0)

#for i in range(n): print(check_wrongs[i])

total_wrongs = [[0 for __ in range(m-7)] for _ in range(n)] #the total amount of wrongs that the chessboard can have at each section
for i in range(n):
    for t in range(m-7):
        total_wrongs[i][t] = sum(check_wrongs[i][t:t+8])

#for i in range(n): print(total_wrongs[i])

min_sum = 99999
for i in range(m-7):
    for t in range(n-7):
        sum = 0
        for j in range(t, t+8):
            sum += total_wrongs[j][i]
        if sum > 32: sum = 64 - sum
        if min_sum > sum: min_sum = sum

print(min_sum)