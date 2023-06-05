N = int(input())
temp = 0

start = N - len(str(N)) * 9
if start < 0:
    start = 0

while start <= N:
    temp = [int(i) for i in str(start)]
    if start + sum(temp) == N:
        print(start)
        break
    start += 1

if start >= N:
    print(0)
