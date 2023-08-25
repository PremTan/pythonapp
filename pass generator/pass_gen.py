import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password by randomly selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Usage example
password_length = 10
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
