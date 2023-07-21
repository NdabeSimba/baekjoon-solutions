while True:
    n = int(input())
    num_list = list()

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            num_list.append(i)

    if sum(num_list) == n:
        print(n, "=", " + ".join(str(i) for i in num_list))
    else:
        print(n, "is NOT perfect.")
