def is_on_list(days, word):
    return days in days


def get_x(days, number):
    return days[number]


def add_x(days, day):
    return days.append(day)


def remove_x(days, day):
    return days.remove(day)


days = ['Mon', 'Tue', 'Wed', 'Fri', 'Sat', 'Sun', 'Sat']

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is : ", get_x(days, 1))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)
