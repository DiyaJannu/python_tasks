# Initial user list
users = [
    {"id": 1, "name": "riya", "email": "riya@example.com"},
    {"id": 2, "name": "Bunty", "email": "bunty@example.com"}
]

# Function to create (add) a new user
def add_user(user_id, name, email):
    for user in users:
        if user["id"] == user_id:
            print("User with this ID already exists.")
            return
    users.append({"id": user_id, "name": name, "email": email})
    print("User added successfully.")

# Function to read (get) a user by ID
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# Function to update a user's name and/or email by ID
def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            print("User updated successfully.")
            return
    print("User not found.")

# Function to delete a user by ID
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            print("User deleted successfully.")
            return
    print("User not found.")

# Function to display all users
def list_users():
    if not users:
        print("No users available.")
    for user in users:
        print(user)

# Example usage
print("Initial users:")
list_users()

print("\nAdding a new user:")
add_user(3, "Abhinav", "abhinav@example.com")
list_users()

print("\nGetting user with ID 2:")
print(get_user(1))

print("\nUpdating user with ID 1:")
update_user(1, name="ria",email="ria@example.com")
list_users()

print("\nDeleting user with ID 2:")
delete_user(2)
list_users()
