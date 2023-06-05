import math

test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    bridge = math.factorial(M) // (math.factorial(N) * math.factorial(M - N))
    print(bridge)