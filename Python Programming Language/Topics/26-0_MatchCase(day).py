# Switch from C


def day(n):
    match n:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case (
            _
        ):  # "_" is a wildcard that matches any value not matched by previous cases
            return "Invalid day number"


day_number = int(input("Enter a day number (1-7): "))
print(day(day_number))
