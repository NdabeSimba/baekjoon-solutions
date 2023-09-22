import sys

input = sys.stdin.readline

num = int(input())
lis = list(map(int, input().split()))

popd = list()
location = 0

for i in range(num):
    # print(location)
    # print(lis)
    # print(popd)
    temp = lis.index(lis[location])
    temp2 = lis.pop(location)
    popd.append(temp + 1)
    location += temp2
    if location > num:
        location = location % num - 1

print(popd)
