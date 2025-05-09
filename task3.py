import hashlib

# Dictionary to store users in format: {"username": "hashed_password"}
users = {}

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
def register(username, password):
    if username in users:
        print("Username already exists.")
    else:
        hashed = hash_password(password)
        users[username] = hashed
        print("Created new user.")

# Function to login a user
def login(username, password):
    hashed = hash_password(password)
    if username in users and users[username] == hashed:
        print("Login successful.")
    else:
        print("Invalid username or password.")

# Example usage
register("diya", "mypassword")         # Output: Created new user.
login("diya", "mypassword")            # Output: Login successful.
login("diya", "wrongpassword")         # Output: Invalid username or password.
register("diya", "anotherpassword")    # Output: Username already exists.
