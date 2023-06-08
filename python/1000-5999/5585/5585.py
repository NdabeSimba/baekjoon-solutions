import sys

input = sys.stdin.readline

money = int(input())
change = 1000 - money
count = 0
worth = [500, 100, 50, 10, 5, 1]

for i in range(6):
    count += change // worth[i]
    change %= worth[i]

print(count)
