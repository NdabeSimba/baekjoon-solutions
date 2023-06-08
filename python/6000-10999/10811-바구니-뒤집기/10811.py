N, M = map(int, input().split())
basket = []

for i in range(N):
    basket.append(i+1)

for _ in range(M):
    i, j = map(int, input().split())
    basket = basket[:i-1] + basket[i-1:j][::-1] + basket[j:]
    
print(*basket)
