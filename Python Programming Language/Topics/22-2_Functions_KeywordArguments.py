# 1.
def hello(greeting, title, firstname, lastname):
    print(f"{greeting} {title} {firstname} {lastname}")


print("1.")
hello("Hello", lastname="Heart", firstname="Strange", title="Mr.")
print("\n")


# 2.
print("2.")
for i in range(1, 6):
    print(
        i, end=" "
    )  # end=" " is also a keyword argument, it is used to print the output in the same line with a space between them.

# 3.
print("\n\n3.")
print(
    "1", "2", "3", sep="|", end="\n\n"
)  # sep="|" is also a keyword argument, it is used to print the output with a separator between them.


# Example of a function with keyword arguments
def phone_number(country_code, area_code, number):
    return f"+{country_code} ({area_code}) {number}"


phone = phone_number(country_code=1, area_code=123, number=4567890)
print(phone)
