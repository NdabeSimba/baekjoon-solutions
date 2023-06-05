# https://www.acmicpc.net/problem/8958

num = int(input())

for _ in range(num):
    prob_list = list(input()) + ['']
    score = 0
    temp = 0

    for i in range(len(prob_list)):
        if prob_list[i] == 'O':
            temp += 1
            score += temp
            if prob_list[i+1] == 'O':
                continue
            else:
                temp = 0
        else:
            pass
    print(score)