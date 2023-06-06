import sys

input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
comp = list(map(int, input().split()))


def binary_search(target, arr, start, end):
    if start > end:
        return 0
    
    mid = (start+end)//2
    
    if target == arr[mid]:
        # return arr[start : end + 1].count(target)
        return count.get(target)
    # .count() time complexity: O(n)
    # .get() time complexity: O(1)

    elif target < arr[mid]:
        return binary_search(target, arr, start, mid-1)
    else:
        return binary_search(target, arr, mid+1, end)
    
count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for i in comp:
    print(binary_search(i, cards, 0, len(cards)-1), end=' ')