num = int(input())
final_num = num
count = 0

while True :
    front = int(num / 10)
    back = num - (front * 10)
    plus = front + back
    num = back * 10 + (plus % 10)
    count = count + 1
    if num == final_num:
        print(count)
        break