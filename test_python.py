import sys
import itertools
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    num = int(input().strip())
    arr = ['A', 'B', 'C']
    nPr = itertools.permutations(arr, 2)
    print(len(list(nPr)))