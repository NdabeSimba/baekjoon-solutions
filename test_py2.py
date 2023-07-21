while True:
    num1, num2 = map(int, input().split())

    if num1 == num2 == 0:
        break

    if num1 > num2:
        if num1 % num2 == 0:
            print("multiple")
        else:
            print("neither")
        continue

    if num1 < num2:
        if num2 % num1 == 0:
            print("factor")
        else:
            print("neither")
        continue
