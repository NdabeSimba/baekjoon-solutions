import sys
input = sys.stdin.readline

N = int(input())
outp = []
stack = []
temp = True
count = 1

for _ in range(N):
    num = int(input())
    
    while count <= num:
        outp.append('+')
        stack.append(count)
        count += 1

    if stack[-1] == num:
        outp.append('-')
        stack.pop()
    
    else:
        temp = False
        break

if temp:
    for i in outp:
        print(i)
else:
    print("NO")
