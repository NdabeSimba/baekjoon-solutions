import sys
input = sys.stdin.readline

def movie_name(n):
    count = 0
    mov_name = 666

    while True:

        if '666' in str(mov_name):
            count += 1

        if count == n:
            return mov_name
        
        mov_name += 1

N = int(input())
print(movie_name(N))