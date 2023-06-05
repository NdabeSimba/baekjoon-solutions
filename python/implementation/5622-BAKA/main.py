# 1
word = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
result = 0
for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            result += dial.index(j) + 3
print(result)

# 2
word = input()
res = 0
for j in word:
    res += int(*[i for i in range(len(dial)) if j in dial[i]]) + 3
print(res)