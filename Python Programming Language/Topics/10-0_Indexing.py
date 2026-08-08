credit_number = "1234-5678-9101-2345"

print(f"The first digit in {credit_number} : {credit_number[0]}") #Start with 0
print(f"The first 4 digit in {credit_number} : {credit_number[:5]}") #Putthing nothing brfore ':' python take it as 0 default
print(f"The next 4 digits in {credit_number} : {credit_number[5:9]}") 
print(f"The credit_number {credit_number} with skiping one digit : {credit_number[::2]}")
print(f"Reverse of {credit_number} : {credit_number[-1::-1]}")