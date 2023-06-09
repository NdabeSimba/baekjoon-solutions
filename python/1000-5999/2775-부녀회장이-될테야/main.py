import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):  
    floor = int(input())
    num = int(input())
    floor_list = [x + 1 for x in range(num)]

    for k in range(floor):
        for n in range(1, num):
            floor_list[n] += floor_list[n - 1]
            
    print(floor_list[-1])