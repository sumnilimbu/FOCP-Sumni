def login(username, password):
    with open("passwd.txt", "r") as file:
        return any(f"{username}:{password}" in line for line in file)

if __name__ == "__main__":
    if login(input("Username: "), input("Password: ")):
        print("Access granted.")
   
    
    else:
        print("Access denied.")
