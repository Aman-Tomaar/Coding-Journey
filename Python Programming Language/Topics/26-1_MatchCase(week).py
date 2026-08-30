# Switch from C


def is_weekday(day):
    match day:
        case (
            "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday"
        ):  # "|" is used to match multiple cases i means or.
            return True
        case "Saturday" | "Sunday":
            return False
        case _:
            raise ValueError("Invalid day of the week")


day_name = input("Enter a day of the week: ")
day_name = day_name.capitalize()  # Capitalize the first letter to match the cases
try:
    if is_weekday(day_name):
        print(f"{day_name} is a weekday.")
    else:
        print(f"{day_name} is a weekend day.")
except ValueError as e:
    print(e)
