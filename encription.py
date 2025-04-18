import bcrypt

# Define a fixed salt (not recommended for production use)
FIXED_SALT = b'$2b$12$d49okXVghFH.FiS7FWURbe'

def hash_password(password):
    # Hash the password using the fixed salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), FIXED_SALT)
    return hashed_password


if __name__ == "__main__":
    # Example usage
    password = "try1"
    hashed = hash_password(password)
    print(f"Original password: {password}")+
    print(f"Hashed password: {hashed.decode('utf-8')}")

    # Verify the password
    input_password = "my_secure_password"