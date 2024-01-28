def delete_user(username):
    try:
        with open("passwd.txt", "r") as file:
            # Creating a list excluding the lines with the specified username
            lines = [line for line in file if username not in line]
        
        with open("passwd.txt", "w") as file:
            # Writing back the modified lines to the password file
            file.writelines(lines)
            
        print("User Deleted.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    username = input("Enter username: ")

    try:
        with open("passwd.txt", "r") as file:
            # Checking if the user exists before attempting deletion
            if any(username in line for line in file):
                delete_user(username)
            else:
                print("User not found. Nothing changed.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
