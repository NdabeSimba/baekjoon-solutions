# 1
def howManyGroup(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i] != str[i + 1]:
            count += 1
    return count + 1


def isGroup(str):
    beforeSorted = howManyGroup(str)
    afterSorted = howManyGroup(sorted(str))
    if beforeSorted == afterSorted:
        return True
    else:
        return False


howManyGroupStr = 0

for i in range(int(input())):
    if isGroup(input()):
        howManyGroupStr += 1

print(howManyGroupStr)

# 2
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)
