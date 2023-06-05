import sys

input = sys.stdin.readline


def angle(y2, y1, x2, x1):
    return (y2 - y1) / (x2 - x1)


def Lbuilding(num):
    min_angle = float("INF")
    count = 0
    for i in range(num - 1, -1, -1):
        ang = angle(building[num],building[i],num,i)
        if min_angle > ang:
            min_angle = ang
            count += 1
    return count


def Rbuilding(num):
    max_angle = -float("INF")
    count = 0
    for i in range(num + 1, N):
        ang = angle(building[num],building[i],num,i)
        if max_angle < ang:
            max_angle = ang
            count += 1
    return count


if __name__ == "__main__":
    N = int(input())
    building = list(map(int, input().split()))

    result = 0

    for i in range(N):
        left = Lbuilding(i)
        right = Rbuilding(i)

        result = max(result, left + right)

    print(result)
