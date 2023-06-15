import sys
input = sys.stdin.readline

def parentheses(s):
    stack = []
    for char in s:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            else:
                return False
    return not stack

parentheses_lis = ['(', ')', '[', ']', '{', '}']

while True:
    temp = ''
    inp = input().rstrip()
    if inp == '.':
        break
    else:
        for i in inp:
            if i in parentheses_lis:
                temp += i
        if parentheses(str(temp)):
            print('yes')
        else:
            print('no')
