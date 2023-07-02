num = int(input())
lis = [0, 1]

for x in range(2, num + 1):
    lis.append(lis[x - 1] + lis[x - 2])

print(lis[num])
