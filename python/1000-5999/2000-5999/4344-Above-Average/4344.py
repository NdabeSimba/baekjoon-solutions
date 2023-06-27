import sys
input = sys.stdin.readline

num = int(input())

for _ in range(num):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]
    
    count = 0
    for i in scores[1:]:
        if i > avg:
            count += 1
            
    percent = (count / scores[0]) * 100
    print('%.3f' % percent + '%')