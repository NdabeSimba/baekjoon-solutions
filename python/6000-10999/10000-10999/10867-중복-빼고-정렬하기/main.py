input = __import__("sys").stdin.readline
num = int(input())
num_list = sorted(set(map(int, input().split())))
print(*num_list)