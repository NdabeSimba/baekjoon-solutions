import sys
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
R = H/2
count = 0

for _ in range(P):
    a, b = map(int, input().split())
    if X <= a <= X + W and Y <= b <= Y + H:
        count += 1
        continue

    elif (((a-X)**2 + (b-(Y+R))**2)**0.5) <= R or (((a-(X+W))**2 + (b-(Y+R))**2)**0.5) <= R:
        count += 1

print(count)