import random
import string

def generate_password(length):
    chars =  string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Password length must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.") 
    password = generate_password(length)
    print("Generated password:", password)


main()