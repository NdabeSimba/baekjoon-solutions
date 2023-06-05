import sys
input = sys.stdin.readline

num, cut = map(int,input().split())
score = sorted(list(map(int,input().split())), reverse = True)

print(score[cut-1])