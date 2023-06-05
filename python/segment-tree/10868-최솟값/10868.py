# import sys
# num_list, num_range = map(int,sys.stdin.readline().split())
# lis = []

# for _ in range(num_list):
#     lis.append(int(sys.stdin.readline()))

# for _ in range(num_range):
#     a, b = map(int, sys.stdin.readline().split())
#     numlis = []
#     for i in range(a,b):
#         numlis.append(lis[i])
#     print(min(numlis))

# in order to solve timeout problem, used segment tree method.
# https://book.acmicpc.net/ds/segment-tree
# source 6

# import sys
# import math
# input = sys.stdin.readline
# def init(a, node, start, end):
#     if start == end:
#         tree[node] = a[start]
#     else:
#         init(a, node*2, start, (start+end)//2)
#         init(a, node*2+1, (start+end)//2+1, end)
#         tree[node] = tree[node*2] + tree[node*2+1]

# def update(a, node, start, end, index, val):
#     if index < start or index > end:
#         return
#     if start == end:
#         a[index] = val
#         tree[node] = val
#         return
#     update(a, node*2, start, (start+end)//2, index, val)
#     update(a, node*2+1, (start+end)//2+1, end, index, val)
#     tree[node] = tree[node*2] + tree[node*2+1]
        
# def query(node, start, end, left, right):
#     if left > end or right < start:
#         return 0
#     if left <= start and end <= right:
#         return tree[node]
#     lmin = query(node*2, start, (start+end)//2, left, right)
#     rmin = query(node*2+1, (start+end)//2+1, end, left, right)
#     return lmin + rmin

# n, m, k = map(int, input().split())
# a = [int(input()) for _ in range(n)]
# h = math.ceil(math.log2(n))
# tree_size = 1 << (h+1)
# tree = [0] * tree_size
# m += k
# init(a, 1, 0, n-1)
# for _ in range(m):
#     what, t1, t2 = map(int, input().split())
#     if what == 1:
#         index, val = t1, t2
#         update(a, 1, 0, n-1, index-1, val)
#     else:
#         left, right = t1, t2
#         print(query(1, 0, n-1, left-1, right-1))

import sys
import math
input = sys.stdin.readline

# reset
def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = min(init(node*2, start, (start+end)//2) , init(node*2+1, (start+end)//2+1, end))
        return tree[node]

# min query
def query(node, start, end, left, right):
    if left > end or right < start:
        return 1000000000
    
    if left <= start and end <= right:
        return tree[node]
    
    lmin = query(node*2, start, (start + end)//2, left, right)
    rmin = query(node*2+1, (start + end)//2+1, end, left, right)
    return min(lmin , rmin)

n, m = map(int,input().split())

# segment tree size
height = int(math.ceil(math.log2(n)))
tree_size = 1 << (height+1)
tree = [0] * tree_size
arr = []

for _ in range(n):
    arr.append(int(input()))

init(1,0,n-1)

for _ in range(m):
    a, b = map(int,input().split())
    print(query(1, 0, n-1, a-1, b-1))
    # thank you google