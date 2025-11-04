# The match statement (introduced in Python 3.10) is Python’s version of a switch-case structure.

def week(day):
    match day:
        case 1:
            return f"The day is Sunday"
        case 2:
            return f"The day is Monday"
        case 3:
            return f"The day is Tuesday"
        case 4:
            return f"The day is Wednesday"
        case 5:
            return f"The day is Thursday"
        case 6:
            return f"The day is Friday"
        case 7:
            return f"The day is Saturday"
        case _:
            return "Invalid number"
        
a=100
while (a>8):
    a=int(input("Enter a day in the week:"))
    print(week(a))
