import sys
input = sys.stdin.readline

N = int(input())

def def_round(n):
    return int(n) + 1 if n - int(n) >= 0.5 else int(n)

if N:
    op_list = [int(input()) for _ in range(N)]
    op_list.sort()

    div_num = def_round(N * 0.15)
    use_list = sorted(op_list)[div_num : N - div_num]

    result = def_round(sum(use_list) / len(use_list))
    print(result)
    
else:
    print(0)