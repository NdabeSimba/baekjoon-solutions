# import sys
# from collections import deque


# input = sys.stdin.readline
# num = int(input())
# deq = deque()

# for _ in range(num):
#     inp = list(map(int, input().split()))

#     if inp[0] == 1:
#         deq.appendleft(inp[1])

#     elif inp[0] == 2:
#         deq.append(inp[1])

#     elif inp[0] == 3:
#         if deq:
#             print(deq.popleft())
#         else:
#             print(-1)

#     elif inp[0] == 4:
#         if deq:
#             print(deq.pop())
#         else:
#             print(-1)

#     elif inp[0] == 5:
#         print(len(deq))

#     elif inp[0] == 6:
#         if len(deq) == 0:
#             print(1)
#         else:
#             print(0)

#     elif inp[0] == 7:
#         if deq:
#             print(deq[0])
#         else:
#             print(-1)

#     elif inp[0] == 8:
#         if deq:
#             print(deq[-1])
#         else:
#             print(-1)


""" Type your code here. """
# total = 0

# for i in range(3):
#     price, width, length = map(float, input().split())
#     width = int(width)
#     length = int(length)

#     Room = width * length
#     Carpet = Room * 1.2 * price
#     Labor = Room * 0.75

#     print("Order #" + str(i + 1))
#     print(f"Room: {Room} sq ft")
#     print(f"Carpet: ${Carpet:.2f}")
#     print(f"Labor: ${Labor:.2f}")
#     print(f"Tax: ${Carpet * (7/100) + Labor * (7/100):.2f}")
#     print(f"Cost: ${(Carpet + Carpet * (7/100)) + (Labor + Labor * (7/100)):.2f}")
#     print("")

#     total += (Carpet + Carpet * (7 / 100)) + (Labor + Labor * (7 / 100))

# print(f"Total Sales: ${total:.2f}")

# import math
# week_total = 0
# days = ["Friday Night Party", "Saturday Night Party", "Sunday Night Party"]

# for i in range(2):
#     nop, aspp, coap = map(float, input().split())

#     num_pizza = math.ceil(nop * aspp / 8)
#     cost = num_pizza * coap
#     tax = cost * 0.07
#     total_cost = cost + tax
#     delivery = total_cost * 0.2
#     total = total_cost + delivery

#     print(days[i])
#     print(f"{num_pizza} Pizzas: ${cost:.2f}")
#     print(f"Tax: ${tax:.2f}")
#     print(f"Delivery: ${delivery:.2f}")
#     print(f"Total: ${total:.2f}")
#     print("")

#     week_total += total

# print(f"Weekend Total: ${week_total:.2f}")

# input_month = input()
# input_day = int(input())

# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# odd_months = ["January", "March", "May", "July", "August", "October", "December"]
# even_months = ["February", "April", "June", "September", "November"]

# if input_month in odd_months and (input_day > 31 or input_day < 1):
#     print("Invalid")

# elif input_month in even_months and (input_day > 30 or input_day < 1):
#     print("Invalid")

# elif input_month in months:
#     temp = months.index(input_month)
#     if 2 <= temp <= 5:
#         if temp == 2 and input_day < 20:
#             print("Winter")
#         elif temp == 5 and input_day > 20:
#             print("Summer")
#         else:
#             print("Spring")
#     elif 6 <= temp <= 8:
#         if temp == 8 and input_day > 21:
#             print("Autumn")
#         else:
#             print("Summer")
#     elif 9 <= temp <= 11:
#         if temp == 11 and input_day > 20:
#             print("Winter")
#         else:
#             print("Autumn")
#     else:
#         print("Winter")

# else:
#     print("Invalid")

# ''' Type your code here. '''
# money = int(input())

# if money == 0:
#     print("No change")

# Dollars = Quarters = Dimes = Nickels = Pennies = 0

# Dollars += money // 100
# money = money % 100

# Quarters += money // 25
# money = money % 25

# Dimes += money // 10
# money = money % 10

# Nickels += money // 5
# money = money % 5

# Pennies += money

# if Dollars > 0:
#     print(Dollars, "Dollars" if Dollars > 1 else "Dollar")
# if Quarters > 0:
#     print(Quarters, "Quarters" if Quarters > 1 else "Quarter")
# if Dimes > 0:
#     print(Dimes, "Dimes" if Dimes > 1 else "Dime")
# if Nickels > 0:
#     print(Nickels, "Nickels" if Nickels > 1 else "Nickel")
# if Pennies > 0:
#     print(Pennies, "Pennies" if Pennies > 1 else "Penny")


year = int(input())
result = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            result = True
    else:
        result = True

print(year,"- leap year") if result else print(year, "- not a leap year")