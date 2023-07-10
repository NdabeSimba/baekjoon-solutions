input = __import__("sys").stdin.readline
num_set = set(range(1, 10000))
rid_set = set()

def self_num(n):
    return n + sum(map(int, str(n)))

for num in range(1, 10001):
    rid_set.add(self_num(num))

result = num_set - rid_set
print(*sorted(result), sep="\n")