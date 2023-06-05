lis = [[''] * 15 for i in range(5)]

for i in range(5):
    line = list(input())
    for j in range(len(line)):
        lis[i][j] = line[j]

for i in range(15):
    for j in range(5):
        if lis[j][i] == '':
            continue
        else:
            print(lis[j][i], end='')