import sys
input = sys.stdin.readline

num, money = map(int, input().split())
worth = []
count = 0

for _ in range(num):
    worth.insert(0, int(input()))

for i in range(num):
    count += money // worth[i]
    money %= worth[i]

print(count)