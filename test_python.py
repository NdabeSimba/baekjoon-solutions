def grade(n):
    if n in [i for i in range(97, 101)]:
        return "A+"
    elif n in [i for i in range(90, 97)]:
        return "A"
    elif n in [i for i in range(87, 90)]:
        return "B+"
    elif n in [i for i in range(80, 87)]:
        return "B" 
    elif n in [i for i in range(77, 80)]:
        return "C+"
    elif n in [i for i in range(70, 77)]:
        return "C" 
    elif n in [i for i in range(67, 70)]:
        return "D+"
    elif n in [i for i in range(60, 67)]:
        return "D" 
    else:
        return "F"

for _ in range(int(input())):
    name, score = map(str, input().split())
    print(name, grade(int(score)))