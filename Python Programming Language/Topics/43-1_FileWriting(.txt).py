"""
w = write & overwrite the existing data
x = create and write in a file [ if used in the place of r where the file already exist it will give an error]
a = append the file and writes the new data after the existing one
"""

emps = ["Strange", "Heart", "Ghevar", "Coco"]
file_path = "C:\\Coding\\test.txt"
try:
    with open(file_path, "w") as file:
        for emp in emps:
            file.write(emp + " ")
        print("The text file was created")
except FileExistsError:
    print("File Already Exists")
