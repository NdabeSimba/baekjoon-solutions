class PhonePlan:
    # FIXME add constructor

    ''' Your solution goes here '''
    def __init__(self, num_mins=0, num_messages=0):
        self.num_mins = num_mins
        self.num_messages = num_messages

    def print_plan(self):
        print(f'Mins: {self.num_mins}', end=' ')
        print(f'Messages: {self.num_messages}')


my_plan = PhonePlan(int(input()), int(input()))
dads_plan = PhonePlan()
moms_plan = PhonePlan(int(input()))

print('My plan...', end=' ')
my_plan.print_plan()

print('Dad\'s plan...', end=' ')
dads_plan.print_plan()

print('Mom\'s plan...', end= ' ')
moms_plan.print_plan()


class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        minute_string = str(self.minutes)
        if self.minutes < 10:
            minute_string = f'0{minute_string}'
        return f'{self.hours} {minute_string}' 

one_hour = Duration(1, 0)
print(one_hour)


class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __eq__(self, other):
        return (self.hours == other.hours) and (self.minutes == other.minutes)

workday = Duration(9, 30)
monday_time = Duration(8, 0)
tuesday_time = Duration(9, 30)

print(tuesday_time == workday)
print(monday_time == workday)


class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
        return False

workday = Duration(7, 0)
monday_time = Duration(9, 0)
tuesday_time = Duration(6, 30)
wednesday_time = Duration(7, 0)

print(monday_time < workday)
print(tuesday_time < workday)
print(wednesday_time < workday)
print(wednesday_time < monday_time)

class CarRecord:
    def __init__(self):
        self.year_made = 0
        self.car_vin = ''

    # FIXME add __str__()

    ''' Your solution goes here '''
    def __str__(self):
	    return (f'Year: {self.year_made}, VIN: {self.car_vin}')

my_car = CarRecord()
my_car.year_made = int(input())
my_car.car_vin = input()

print(my_car)