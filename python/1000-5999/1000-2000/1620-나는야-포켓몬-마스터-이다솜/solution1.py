import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poke_di = dict()
poke_set = list()

for i in range(N):
    name = input().strip()
    poke_di[name] = i
    poke_set.append(name)

for i in range(M):
    find = input().strip()
    try:
        print(poke_set[int(find) - 1])
    except:
        print(poke_di[find] + 1)