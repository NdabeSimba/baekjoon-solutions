for x, y in sorted([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda x: (x[0], x[1])):
    print(x, y)