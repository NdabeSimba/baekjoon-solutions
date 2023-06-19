import sys
input = sys.stdin.readline

N = int(input())
count = 1
mov_name = 666

while count != N:
    mov_name += 1
    if '666' in str(mov_name):
        count += 1
    
print(mov_name)