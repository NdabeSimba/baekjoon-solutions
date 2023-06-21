import sys

for line in sys.stdin:
    y1, y2, af = map(int, line.split())

    if af == 0:
        break

    if y1 == y2 == 0:
        print(0)
        
    else:
        for _ in range(af):
            y1, y2 = y2, y1 + y2
        print(y2)