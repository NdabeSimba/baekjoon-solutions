import sys
input = sys.stdin.readline

N = int(input())
time = list(map(int, input().split()))
young = mins = 0

for t in time:
    young += (t // 30 + 1) * 10
    mins += (t // 60 + 1) * 15

if mins == young:
    print("Y M", mins)

elif mins < young:
    print("M", mins)

else:
    print("Y", young)