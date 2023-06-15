import sys
input = sys.stdin.readline

N = int(input())

peo_lis = []
count = 0

for i in range(N):
    inp = input().rstrip()

    if inp == 'ENTER':
        count += len(list(set(peo_lis)))
        peo_lis = []
    
    else:
        peo_lis.append(inp)

count += len(list(set(peo_lis)))
    
print(count)