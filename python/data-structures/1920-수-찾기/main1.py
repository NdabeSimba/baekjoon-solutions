N = int(input())
num_lis = sorted(list(map(int, input().split())))
M = int(input())
compare = list(map(int, input().split()))


def binary_search(target, data):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True

        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


for i in compare:
    if binary_search(i, num_lis):
        print(1)
    else:
        print(0)
