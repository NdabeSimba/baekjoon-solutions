import sys
input = sys.stdin.readline

while True:
    num_lis = sorted(list(map(int,input().split())))

    if sum(num_lis) == 0:
        break
    elif (num_lis[2]**2 == (num_lis[1]**2 + num_lis[0]**2)):
        print('right')
        pass
    else:
        print('wrong')
        pass