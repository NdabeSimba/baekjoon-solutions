import sys
input = sys.stdin.readline

num_list1 = []
num_list2 = []

for _ in range(3):
    num1, num2 = map(int, input().split())

    if num1 in num_list1:
        num_list1.remove(num1)
    else:
        num_list1.append(num1)

    if num2 in num_list2:
        num_list2.remove(num2)
    else:
        num_list2.append(num2)

print(*num_list1, *num_list2)