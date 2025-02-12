# User database (in-memory storage, not suitable for production)
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

# Function to register a new user
def register():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Try again.")
        return
    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful!")

# Function to authenticate a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful! Welcome, " + username + "!")
    else:
        print("Login failed. Invalid username or password.")

# Main program loop
while True:
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
