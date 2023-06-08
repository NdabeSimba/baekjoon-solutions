import sys
read = sys.stdin.readline

def main():
    n = int(read())
    coord = [list(map(int, read().split())) for _ in range(n)]
    coord.sort(key=lambda x: (x[0], x[1]))

    for i in range(n):
        print(coord[i][0], coord[i][1])

main()