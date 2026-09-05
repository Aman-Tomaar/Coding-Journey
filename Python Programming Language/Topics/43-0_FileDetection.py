import os

file_path = "C:\\Coding\\Python Programming Language\\Topics\\car.py"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("It is a File")
    elif os.path.isdir(file_path):
        print("It is a Directory (Folder)")
else:
    print(f"The location '{file_path}' doesn't exist")
