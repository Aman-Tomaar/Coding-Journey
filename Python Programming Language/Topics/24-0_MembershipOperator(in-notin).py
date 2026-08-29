# in and not in used to find the membership of a value in a sequence (list, tuple, string, etc.)
# example

fruit = "apple"

user_input = input("Enter a fruit name: ")
if user_input in fruit:
    print(f"{user_input} is present in the fruit.")
elif user_input not in fruit:
    print(f"{user_input} is not present in the fruit.")

students = ["Alice", "Bob", "Charlie", "David"]
user_input = input("Enter a student name: ")
user_input = (
    user_input.capitalize()
)  # Capitalize the first letter of the input to match the list format
if user_input in studets:
    print(f"{user_input} is present in the students list.")
elif user_input not in studets:
    print(f"{user_input} is not present in the students list.")
