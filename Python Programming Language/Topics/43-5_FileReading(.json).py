import json

file_path = "C:\\Coding\\test.json"
try:
    with open(file_path, "r") as file:
        contents = json.load(
            file
        )  # just the diff b/w rxr file and json is file.read() and json.load()
        print(contents)
        print(contents["name"])  # can use keys to the value of them
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
