import sys
input = sys.stdin.readline

num = int(input())
num_list = list(map(int,input().split()))
num_list_sort = list(sorted(set(num_list)))

num_dic = {num_list_sort[i]: i for i in range (len(num_list_sort))}

for i in num_list:
  print(num_dic[i],end=' ')