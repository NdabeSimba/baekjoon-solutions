num_stu = int(input())
order = list(map(int, input().split()))
line = []

for i in range(num_stu):
    if order[i] == 0:
        line.append(i+1)
    else:
        line.insert(i-order[i],i+1)
        
print(*line)