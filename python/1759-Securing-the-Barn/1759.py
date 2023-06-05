# from itertools import permutations
# import sys
# input = sys.stdin.readline
# L, C = map(int, input().split())
# per = permutations(range(1, L+1), C)
# for i in per:
#     print(" ".join(map(str, i)))


# import itertools
# if __name__ == '__main__':
#     L, C = map(int, input().split())
#     s = map(str,input().split())
#     words = sorted(list(s))
#     permutations = list(itertools.permutations(words, L))
#     print(*[''.join(permutation) for permutation in permutations],sep="\n")


import sys
from itertools import combinations

def make_code():
    result = []
    for C in list(combinations(words, L)):
        vowel_cnt = consonants_cnt = 0
        for word in C:
            if word in vowels:
                vowel_cnt += 1
            else:
                consonants_cnt += 1
        if vowel_cnt > 0 and consonants_cnt > 1:
            result.append("".join(C))
    return result

L, C = map(int, sys.stdin.readline().split())
words = sorted(sys.stdin.readline().split())

vowels = set(['a', 'e', 'i', 'o', 'u'])

for p in make_code():
    print(p)


import itertools
import sys

input = sys.stdin.readline
vowel = ["a", "e", "i", "o", "u"]

if __name__ == "__main__":
    L, C = map(int, input().split())
    s = map(str, input().split())

    words = sorted(list(s))
    result = []
    combinations = list(itertools.combinations(words, L))

    for combination in combinations:
        vowel_cnt = consonants_cnt = 0
        for word in combination:
            if word in vowel:
                vowel_cnt += 1
            else:
                consonants_cnt += 1

        if vowel_cnt > 0 and consonants_cnt > 1:
            result.append("".join(combination))

print(*result, sep="\n")
