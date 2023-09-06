import sys

input = sys.stdin.readline
num = int(input())
de = list()

for _ in range(num):
    lis = list(map(int, input().split()))

    if lis[0] == 1:
        de.append(lis[1])

    elif lis[0] == 2:
        if de:
            print(de.pop())
        else:
            print(-1)
    
    elif lis[0] == 3:
        print(len(de))
    
    elif lis[0] == 4:
        if de:
            print(0)
        else:
            print(1)
    
    elif lis[0] == 5:
        if de:
            print(de[-1])
        else:
            print(-1)