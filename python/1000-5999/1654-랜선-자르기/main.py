import sys
input = sys.stdin.readline

K, N = map(int, input().split())
length = [int(input()) for _ in range(K)]

left, right = 1, max(length)
result = 0

while left <= right:
    mid = (left + right) // 2
    total = 0

    for leng in length:
        total += leng // mid

    if total >= N:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)