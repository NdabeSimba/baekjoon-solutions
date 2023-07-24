while True:
    num_list = sorted(list(map(int, input().split())))

    if num_list[0] == num_list[1] == num_list[2] == 0:
        break

    if num_list[2] >= num_list[1] + num_list[0]:
        print("Invalid")
        
    elif num_list[0] == num_list[1] == num_list[2]:
        print("Equilateral")

    elif (
        num_list[0] == num_list[1]
        or num_list[1] == num_list[2]
        or num_list[2] == num_list[0]
    ):
        print("Isosceles")

    else:
        print("Scalene")
