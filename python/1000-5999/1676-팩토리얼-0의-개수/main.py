import sys
input = sys.stdin.readline

N = int(input())

def factorial(n):
    result = 1
    for i in range(n):
        result *= i + 1

    return result

comp = list(str(factorial(N)))
count = 0

for num in reversed(range(len(comp))):
    if comp[num] == '0':
        count += 1
    else:
        break

print(count)