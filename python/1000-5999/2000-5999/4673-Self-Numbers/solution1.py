input = __import__("sys").stdin.readline
num_list = list(range(1, 10000))
rid_set = set()

for num in num_list:
    temp = num
    for n in str(temp):
        temp += int(n)

    if temp < 10000:
        rid_set.add(temp) 

for num in rid_set:
    num_list.remove(num)

print(*num_list, sep="\n")