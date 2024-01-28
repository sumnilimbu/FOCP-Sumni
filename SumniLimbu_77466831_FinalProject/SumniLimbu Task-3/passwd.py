def change_password(username, current_password, new_password):
    try:
        with open("passwd.txt", "r") as file:
            lines = [line.replace(f"{username}:{current_password}", f"{username}:{new_password}") for line in file]

        with open("passwd.txt", "w") as file:
            file.writelines(lines)
            
        print("Password changed.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        username = input("Username: ")
        current_password = input("Current Password: ")

        while True:
            new_password = input("New Password: ")
            confirm_password = input("Confirm: ")

            if new_password == confirm_password and new_password:
                break
            elif not new_password:
                print("Password cannot be empty. Please enter a password.")
            else:
                print("Passwords do not match. Please try again.")

        with open("passwd.txt", "r") as file:
            if any(f"{username}:{current_password}" in line for line in file):
                change_password(username, current_password, new_password)
            else:
                print("Invalid current password. Nothing changed.")
    except Exception as e:
        print(f"An error occurred: {e}")
