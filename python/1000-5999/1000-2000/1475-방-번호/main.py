num = list(map(int, input()))
lis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 1

for n in num:
    new_lis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_lis.remove(n)

    if n in lis:
        lis.remove(n)
    else:
        if n == 6:
            if 9 in lis:
                lis.remove(9)
            else:
                count += 1
                lis.extend(new_lis)
        elif n == 9:
            if 6 in lis:
                lis.remove(6)
            else:
                count += 1
                lis.extend(new_lis)
        else:
            count += 1
            lis.extend(new_lis)

print(count)