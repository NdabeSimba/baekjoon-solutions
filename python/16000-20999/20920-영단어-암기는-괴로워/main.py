import sys; input = sys.stdin.readline

i, j = map(int, input().split())
wd = dict()

for i in range(i):
    word = input().rstrip()
    if len(word) >= j:
        if word in wd:
            wd[word] = wd[word] + 1
        else:
            wd[word] = 1

temp = sorted(wd.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for k,v in temp:
    print(k)