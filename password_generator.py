import random
import string

def input_yes_or_no(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ['yes', 'no']:
            return user_input
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def generate_password(length, use_letters, use_digits, use_punctuation):
    chars = ''
    if use_letters:
        chars += string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_punctuation:
        chars += string.punctuation
    if not chars:
        raise ValueError("No character types selected!")
    
    password = "".join(random.choice(chars) for _ in range(length))
    return password


def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 3:
                print("Password length must be greater than 3.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    use_letters = input_yes_or_no("Do you want to use letters? (yes/no): ") == 'yes'
    use_digits = input_yes_or_no("Do you want to use digits? (yes/no): ") == 'yes'
    use_punctuation = input_yes_or_no("Do you want to use punctuation? (yes/no): ") == 'yes'
    

    try:
        password = generate_password(length, use_letters, use_digits, use_punctuation)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
    
                    
    