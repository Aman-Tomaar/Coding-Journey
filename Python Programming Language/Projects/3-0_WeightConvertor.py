w = float(input("Enter your weight: ")) # Fixed spelling of 'weight'
unit = input("Enter Kg[K] OR Pounds[P]: ")

if unit == 'K' or unit == 'k':
    w *= 2.20462
    print(f"Weight in Pounds: {round(w, 2)}")

elif unit == 'P' or unit == 'p':
    w /= 2.20462
    print(f"Weight in Kg: {round(w, 2)}")

else:
    print("Invalid Unit")
