import sys
input = sys.stdin.readline

L = int(input())
M = 1234567891
r = 31

word = list(input().strip())
hash_sum = 0

for i in range(L):
    hash_sum += (ord(word[i]) - 96) * (pow(r, i))

print(hash_sum % M)

# H = (∑ i=0 부터 (l−1) 까지 ai * r^i) mod M

# \[H = \sum_{i=0}^{l-1}{a_ir^i} \mod M\] 