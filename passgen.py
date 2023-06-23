import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = int(input("Enter the desired length of the password: "))
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
