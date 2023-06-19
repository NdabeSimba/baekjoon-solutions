N = int(input())
temp = 0

start = N - len(str(N)) * 9
if start < 0:
    start = 0

for i in range(start, N + 1):
    temp = i + sum(list(map(int, str(i))))
    if temp == N:
        print(i)
        break
    if i == N:
        print(0)
