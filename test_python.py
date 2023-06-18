import sys
input = sys.stdin.readline

for _ in range(3):
    num = 0
    for _ in range(int(input())):
        num += int(input())

    if num == 0:
        print(0)
    else:
        print('+') if num > 0 else print('-')
