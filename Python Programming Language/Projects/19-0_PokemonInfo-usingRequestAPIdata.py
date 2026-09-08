import requests

base_url = "https://pokeapi.co/api/v2/"


def get_poke_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        print(
            f"Failed to retrieve data on this pokemon: {name} | Error Code: {response.status_code}"
        )
        return None


is_running = True

while is_running:
    u_input = (
        input("Enter the name of the pokemon you want to get info on (q to quit): ")
        .strip()
        .lower()
    )

    if u_input == "q":
        print("Goodbye!")
        break

    poke_info = get_poke_info(u_input)

    if poke_info:
        try:
            choice = int(
                input(
                    "Enter what info you want about the pokemon:\n1. ID\n2. Height\n3. Weight\n4. Type\n5. All\nChoice: "
                )
            )
        except ValueError:
            print("Please enter a valid number between 1 and 5.")
            continue

        if choice == 1:
            print(f"ID: {poke_info['id']}")
        elif choice == 2:
            print(f"Height: {poke_info['height']}")
        elif choice == 3:
            print(f"Weight: {poke_info['weight']}")
        elif choice == 4:
            types = [t["type"]["name"] for t in poke_info["types"]]
            print(f"Type(s): {', '.join(types)}")
        elif choice == 5:
            print(f"Name: {poke_info['name'].capitalize()}")
            print(f"ID: {poke_info['id']}")
            print(f"Height: {poke_info['height']}")
            print(f"Weight: {poke_info['weight']}")
            types = [t["type"]["name"] for t in poke_info["types"]]
            print(f"Type(s): {', '.join(types)}")
        else:
            print("Invalid choice!")
