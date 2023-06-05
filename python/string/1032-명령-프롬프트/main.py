import sys
input = sys.stdin.readline

num = int(input())
lis = []
for i in range(num):
    lis.append(input().rstrip())

sen = list(lis[0])
for i in range(num):
    for j in range(len(sen)):
        if sen[j] != lis[i][j]:
            sen[j] = "?"
        else:
            continue

print(*sen,sep='')
