count = 0
for i in range(8):
    board = input()
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0 and board[j] == "F":
                count += 1
    else:
        for j in range(8):
            if j % 2 == 1 and board[j] == "F":
                count += 1
print(count)