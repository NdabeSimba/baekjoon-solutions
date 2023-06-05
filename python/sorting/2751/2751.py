import sys
# used sys.stdin.readline to solve timeout problem
num = int(sys.stdin.readline())
num_list = []

for _ in range(num):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

for i in range(num):
    print(num_list[i])