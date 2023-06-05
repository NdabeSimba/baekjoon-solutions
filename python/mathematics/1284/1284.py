while True:
    num = input()
    result = 1

    if num == '0':
        break

    for i in num:
        if i == '0':
            result += 4
        elif i == '1':
            result += 2
        else:
            result += 3
        result += 1

    print(result)
