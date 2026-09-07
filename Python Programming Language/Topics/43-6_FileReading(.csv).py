import csv

file_path = "C:\\Coding\\test.csv"

try:
    with open(file_path, "r") as file:
        contents = csv.reader(file)  # simple difference is csv.reader()
        print(contents)  # we a memory location
        for line in contents:
            print(line)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
