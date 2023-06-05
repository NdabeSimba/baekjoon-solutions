N = int(input())
count = 0
for i in range(N):
    word = input()
    result = True
    for j in range(len(word) - 1):
        if word[j] != word[j + 1]:
            temp = word[j + 1 :]
            if word[j] in temp:
                result = False
                break
    if result == True:
        count += 1

print(count)
