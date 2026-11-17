
import random
import string

passwords = {}

FILE_PATH = r"C:\Users\HP\OneDrive\Desktop\Operation Switch\Projects\Password Manager Program Py\passwords.txt"

# Load existing passwords
try:
    with open(FILE_PATH, "r") as file:
        for line in file:
            website, pwd = line.strip().split(":", 1)
            passwords[website] = pwd
except FileNotFoundError:
    pass


def generate_pswd():
    chars = string.ascii_letters + string.digits + "@#%$"
    return "".join(random.choice(chars) for _ in range(8))


while True:
    print("\n-----------PERSONAL PASSWORD MANAGER-----------")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Random Password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Save password    
    if choice == "1":
        site = input("Enter Website: ")
        pwd = input("Enter Password: ")

        passwords[site] = pwd

        with open(FILE_PATH, "w") as file:
            for website, password in passwords.items():
                file.write(f"{website}:{password}\n")

        print("Saved successfully!")

    # View passwords
    elif choice == "2":
        if not passwords:
            print("No Data!")
        else:
            for site, pwd in passwords.items():
                print(site, ":", pwd)

    # Generate password
    elif choice == "3":
        print("Generated Password:", generate_pswd())

    # Exit
    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Enter valid Choice!")
