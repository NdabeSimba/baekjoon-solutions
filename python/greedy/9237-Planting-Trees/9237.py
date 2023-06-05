import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
# sorted out in reverse, to count the days going
time.sort(reverse=True)
result = []

for i in range(n):
    result.append(time[i]+ 1 + i)
# i counts as days

print(max(result) + 1)