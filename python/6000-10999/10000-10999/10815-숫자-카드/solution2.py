N = int(input())
card = set(map(int, input().split()))
M = int(input())
distinction = list(map(int, input().split()))

for num in distinction:
    if num in card:
        print(1, end=' ')
    else:
        print(0, end=' ')