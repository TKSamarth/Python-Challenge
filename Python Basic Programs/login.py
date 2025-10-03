username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Access granted")
    else:
        print("Incorrect password")
else:
    print("Username not found")