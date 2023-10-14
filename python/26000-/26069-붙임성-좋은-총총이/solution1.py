import sys; input = sys.stdin.readline

num = int(input())
person = {"ChongChong"}

for _ in range(num):
    per1, per2 = input().rstrip().split()

    if per1 in person:
        person.add(per2)
    if per2 in person:
        person.add(per1)

print(len(person))