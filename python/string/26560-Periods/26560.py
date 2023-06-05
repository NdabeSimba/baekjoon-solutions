num = int(input())
sent = [list(map(str, input().split())) for _ in range(num)]

for i in range(num):
    if sent[i][-1][-1] != ".":
        sent[i][-1] = str(sent[i][-1])+"."
        print(*sent[i])
    else:
        print(*sent[i])
        pass