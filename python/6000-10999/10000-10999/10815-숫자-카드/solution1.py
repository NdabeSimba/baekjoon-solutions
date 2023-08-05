N = int(input())
have_list = sorted(list(map(int, input().split())))

M = int(input())
comp_list = list(map(int, input().split()))


for num in comp_list:
    start, end = 0, N - 1
    result = False
    while start <= end:
        mid = (start + end) // 2
        if have_list[mid] > num:
            end = mid - 1
        elif have_list[mid] < num:
            start = mid + 1
        else:
            result = True
            break
    print(1 if result else 0, end=" ")
