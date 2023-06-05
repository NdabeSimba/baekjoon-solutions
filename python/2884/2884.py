# t, m = [int(x) for x in input().split()]
# if t > 0:
#     if m >= 45:
#         m = m-45
#         print(t, m)
#     elif m < 45:
#         t = t-1
#         m = m+60
#         print(t, m-45)
# elif t == 0:
#     if m >= 45:
#         m = m-45
#         print(t, m)
#     elif m < 45:
#         m = m+60
#         t = 23
#         print(t, m-45)

# better code, better efficiency time-wise
H, M = map(int, input().split())
if M < 45 :
    if H == 0 :
        H = 23
        M += 60
    else :
        H -= 1	
        M += 60
print(H, M-45)	