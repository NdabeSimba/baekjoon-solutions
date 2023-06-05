import sys
input = sys.stdin.readline

num = int(input())
big_bag = 0
smol_bag = 0

while num >= 0:
    if num % 5 == 0:
        big_bag += num // 5
        print(big_bag + smol_bag)
        break
    else:
        smol_bag += 1
        num -= 3
else:
    print(-1)
