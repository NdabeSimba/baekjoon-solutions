num_list = sorted(list(map(int, input().split())))
r = len(num_list)
temp = num_list[0]

while True:
    res = 0

    for i in range(r):
        if temp % num_list[i] == 0:
            res += 1

    if res >= 3:
        break
    else:
        temp += 1

print(temp)