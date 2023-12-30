N, K = map(int, input().split())
yos_lis = list()
num_lis = list(i for i in range(1, N + 1))
ind = 0

for _ in range(N):
    ind += K - 1
    if ind >= len(num_lis):
        ind = ind % len(num_lis)
    yos_lis.append(num_lis.pop(ind))

print(str(yos_lis).replace('[','<').replace(']','>'))