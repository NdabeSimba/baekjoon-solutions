N = int(input())

window = [True]*N
num_set = set()

for i in range(2, N + 1):
    for j in range(1, N + 1):
        temp = i*j
        if temp in num_set:
            num_set.remove(temp)
        else:
            num_set.add(temp)

print(num_set)