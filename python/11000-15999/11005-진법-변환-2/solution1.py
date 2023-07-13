input = __import__("sys").stdin.readline
lis = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())


def solution(num, binary):
    rev_base = ""

    while num > 0:
        num, mod = divmod(num, binary)
        rev_base += lis[mod]

    return rev_base[::-1]


print(solution(N, B))
