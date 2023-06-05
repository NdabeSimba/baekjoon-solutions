num = int(input())
seat = str(input())

count = seat.count('LL')

if 'LL' in seat:
    seat.split(sep='LL')
    print(len(seat) - count + 1)
else:
    print(len(seat))