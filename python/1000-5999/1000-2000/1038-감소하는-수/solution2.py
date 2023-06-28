def recur(N):
    if N == 0:
        return ['9', '']
    
    S = recur(N - 1) #모든 9~1 list
    a = len(S)

    for x in range(a):
        S.append(S[x] + str(9 - N))

    return S

N = int(input())

Final = recur(9) #9~0 list
FinalMody  = []

for x in Final:
    if x == '':
        continue
    FinalMody.append(int(x))

FinalMody.sort()

try: print(FinalMody[N], len(Final), len(FinalMody))
except: print(-1)
