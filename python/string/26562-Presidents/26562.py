# https://www.acmicpc.net/problem/26562

num = int(input())
dic = {
    "Franklin": 100,
    "Grant": 50,
    "Jackson": 20,
    "Hamilton": 10,
    "Lincoln": 5,
    "Washington": 1,
}

name = [list(map(str, input().split())) for _ in range(num)]

for i in range(num):
    mon = 0
    for j in range(len(name[i])):
        mon = mon + int(dic.get(name[i][j]))
    print("$" + str(mon))
