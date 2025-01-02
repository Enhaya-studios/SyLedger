import os

def main():
    entry_name = input("Welcome to sledger! Enter entry name: ")
    entry_type = input("Enter entry type: (account, pin, person specs) ").lower()

    directory = "sledger_data"
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, f"{entry_name}.txt")

    with open(file_path, 'w') as file:
        file.write(f"Name: {entry_name}\n")
        file.write(f"Type: {entry_type}\n")

        if entry_type == "account":
            username = input(f"Enter your username for {entry_name}: (leave blank if not applicable) ")
            email = input(f"Enter your email for {entry_name}: (leave blank if not applicable) ")
            password = input(f"Enter your password for {entry_name}: ")

            file.write(f"Username: {username}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Password: {password}\n")

            print(f"\nDetails saved to {file_path}")

        elif entry_type == "pin":
            pin = input(f"Enter your pin for {entry_name}: ")

            file.write(f"Pin: {pin}\n")

            print(f"\nDetails saved to {file_path}")

        elif entry_type == "person specs":
            name = input(f"Enter {entry_name}'s name: ")
            date_of_birth = input(f"Enter {entry_name}'s date of birth: ")
            phone_number = input(f"Enter {entry_name}'s phone number: ")
            address = input(f"Enter {entry_name}'s address: ")

            file.write(f"Full Name: {name}\n")
            file.write(f"Date of Birth: {date_of_birth}\n")
            file.write(f"Phone Number: {phone_number}\n")
            file.write(f"Address: {address}\n")

            print(f"\nDetails saved to {file_path}")

        else:
            print("Invalid entry type")

if __name__ == "__main__":
    main()
