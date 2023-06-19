import sys
input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]

# 1, 2
print(
    round(sum(num_list) / N),
    sorted(num_list)[N//2], sep="\n"
)

# 3
count = {}
for i in num_list:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
        
max_count = max(count.values())
max_dict = []

for i in count:
    if max_count == count[i]:
        max_dict.append(i)

max_dict.sort()
print(max_dict[1]) if len(max_dict) > 1 else print(max_dict[0])    

# 4
print(0) if N == 1 else print(abs(max(num_list)-min(num_list)))
