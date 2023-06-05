def isPalindrome(x):
    result = "yes"
    for i in range(len(str(x)) // 2):
        if str(x)[i] != str(x)[-i - 1]:
            result = "no"
            break
    return result

while True:
    num = int(input())
    if num == 0:
        break
    else:
        print(isPalindrome(num))
