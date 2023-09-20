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

import math
week_total = 0
days = ["Friday Night Party", "Saturday Night Party", "Sunday Night Party"]

for i in range(2):
    nop, aspp, coap = map(float, input().split())

    num_pizza = math.ceil(nop * aspp / 8)
    cost = num_pizza * coap
    tax = cost * 0.07
    total_cost = cost + tax
    delivery = total_cost * 0.2
    total = total_cost + delivery

    print(days[i])
    print(f"{num_pizza} Pizzas: ${cost:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Delivery: ${delivery:.2f}")
    print(f"Total: ${total:.2f}")
    print("")

    week_total += total

print(f"Weekend Total: ${week_total:.2f}")