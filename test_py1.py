E, S, M = map(int, input().split())

e1, s1, m1 = 1, 1, 1
year = 1

while e1 != E or s1 != S or m1 != M:
    e1 += 1
    s1 += 1
    m1 += 1
    year += 1

    if e1 >= 16:
        e1 -= 15
    if s1 >= 29:
        s1 -= 28
    if m1 >= 20:
        m1 -= 19

print(year)
