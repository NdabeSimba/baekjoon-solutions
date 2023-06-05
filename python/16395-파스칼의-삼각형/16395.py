import sys
input = sys.stdin.readline

n, k = map(int,input().split())
tri = []
calc = []

for i in range(n):
    tri.append(1)
    calc.append(1)
    if i < 2:
        pass
    else:
        for j in range(1, len(tri)-1):
            calc[j] = tri[j-1] + tri[j]
    for l in range(len(tri)):
        tri[l] = calc[l]
    #     print(str(tri[l]) + " ", end="")
    # print("")
print(tri[k-1])