# This is for exception handling in the addUser module

class UserAlreadyExistsError(Exception):
    """Exception raised when trying to add a user that already exists."""
    def __init__(self, username):
        self.username = username
        self.message = f"User '{self.username}' already exists."
        super().__init__(self.message)      

# Example usage:
if __name__ == "__main__":
    try:
        # Simulate adding a user that already exists
        existing_user = "Ittani"
        raise UserAlreadyExistsError(existing_user)
    except UserAlreadyExistsError as e:
        print(e.message)  # Output: User 'john_doe' already exists.
        # Handle the exception (e.g., log it, notify the user, etc.)