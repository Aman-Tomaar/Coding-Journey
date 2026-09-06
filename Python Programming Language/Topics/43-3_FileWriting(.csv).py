import csv

employees = [
    ["Name", "Age", "Job"],
    ["SpongeBob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"],
]

file_path = "test.csv"

try:
    with open(file_path, "x", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
