print("****RLUES FOR CREATING THE USERNAME****\n" \
"1. maximum size of the username must be less than 12 characters\n" \
"2. username cannot contain spaces\n" \
"3. username cannot contain digits\n")

uname = input("Create a Username: ")
if len(uname) > 12:
    print("Username cannot exceed 12 character rule.")
elif not uname.find(" ") == -1:
    print("Username cannot contain " " Spaces.")
elif uname.isalpha() == False:
    print("Username cannot contain digit.")
else: 
    print(f"WELCOME {uname} !!")