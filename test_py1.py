import math

H, W, N, M = map(int, input().split())

Hc = math.ceil(H / (N + 1))
Wc = math.ceil(W / (M + 1))

print(Hc * Wc)