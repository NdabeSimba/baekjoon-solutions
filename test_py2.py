import sys

input = sys.stdin.readline

num = int(input())
lis = list(map(int, input().split()))

popd = list()
location = 0

for i in range(num):
    popd.append(lis.index(lis[location]) + 1)
    temp = lis.pop(location)
    location += temp
    if location > num:
        location = location % num
    print(location)

print(popd)
