import sys
input = sys.stdin.readline

while True:
    a1, a2, b1, b2 = map(int,input().split())
    a_num = max(a1,a2)*10 + min(a1,a2)
    b_num = max(b1,b2)*10 + min(b1,b2)
    
    if a1 == a2 == b1 == b2 == 0:
        break
    elif a_num == 21 or b_num == 21:
        if a_num == b_num == 21:
            print("Tie.")
        else:
            if a_num == 21:
                print("Player 1 wins.")
            else:
                print("Player 2 wins.")
    elif a1 == a2 or b1 == b2:
        if a1 == a2 and b1 != b2:
            print("Player 1 wins.")
        elif b1 == b2 and a1 != a2:
            print("Player 2 wins.")
        elif a1 == a2 and b1 == b2:
            if a1 > b1:
                print("Player 1 wins.")
            elif a1 < b1:
                print("Player 2 wins.")
            else:
                print("Tie.")
    else:
        if a_num > b_num:
            print("Player 1 wins.")
        elif a_num < b_num:
            print("Player 2 wins.")
        else:
            print("Tie.")