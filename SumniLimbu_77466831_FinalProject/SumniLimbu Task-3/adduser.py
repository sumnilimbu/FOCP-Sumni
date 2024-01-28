def add_user(real_name, username, password):
    with open("passwd.txt", "a") as file:
        # Appending the new user entry to the password file
        file.write(f"{real_name}:{username}:{password}\n")

if __name__ == "__main__":
    real_name = input("Enter real name: ")
    username = input("Enter new username: ")

    while True:
        password = input("Enter password: ")
        if password:
            break
        else:
            print("Password cannot be empty. Please enter a password.")

    with open("passwd.txt", "r") as file:
        # Checking if the username already exists
        if any(username in line for line in file):
            print("Cannot add. Most likely username already exists.")
        else:
            add_user(real_name, username, password)
            print("User Created.")