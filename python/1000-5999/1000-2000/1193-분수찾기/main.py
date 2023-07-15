X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

a, b = X, line - X + 1

if line % 2 == 0:
    print("{}/{}".format(a, b))
else:
    print("{}/{}".format(b, a))