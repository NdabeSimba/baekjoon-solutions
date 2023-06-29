input = __import__('sys').stdin.readline

N = int(input())
ch_dict = dict()

for _ in range(N):
    name = input()
    if name[0] in ch_dict:
        ch_dict[name[0]] += 1
    else:
        ch_dict[name[0]] = 1

if max(list(ch_dict.values())) >= 5:
    for ch in sorted(ch_dict):
        if ch_dict[ch] >= 5:
            print(ch, end='')
else:
    print("PREDAJA")