num = int(input())
for i in range(num):
    lis = list(input())
    sum = 0
    for i in lis:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')