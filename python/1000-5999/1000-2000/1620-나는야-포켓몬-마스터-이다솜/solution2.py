import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poke_di = dict()
poke_set = list()

for i in range(1, N + 1):
    name = input().strip()
    poke_di[name] = i
    poke_set.append(name)

for i in range(M):
    find = input().strip()
    if "0" <= find[0] <= "9":
        print(poke_set[int(find) - 1])
    else:
        print(poke_di[find])