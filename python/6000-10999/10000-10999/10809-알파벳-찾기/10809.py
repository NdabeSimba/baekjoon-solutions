# https://www.acmicpc.net/problem/10809

alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alphabet = list(range(97,123)) using ASCII table

inp = input()

for i in alphabet:
    print(inp.find(i), end=' ')
