import sys
input = sys.stdin.readline

num = int(input())
for i in range(num):
    cent = int(input())
    quar = dime = nick = penn = 0
    while cent != 0:
        quar += cent//25
        cent = cent%25
        dime += cent//10
        cent = cent%10
        nick += cent//5
        cent = cent%5
        penn += cent//1
        cent = cent%1
    print(quar, dime, nick, penn)
