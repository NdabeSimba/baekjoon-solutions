N = int(input())
room_count = 1
result = 1

while N > room_count:
    room_count += 6 * result
    result += 1
    
print(result)