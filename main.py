def menu():
    print("Menu")
    print("------------- ")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit \n")


# encodes the password by adding 3 to each string
def encode(value):
    new_value = ""

    for char in value:
        encoded_value = str((int(char) + 3) % 10)
        new_value += encoded_value
    return new_value


# decodes password by subtracting 3 from each string
def decode(password):
    password = int(password)
    password_list = [int(i) for i in str(password)]
    old_password = [i - 3 for i in password_list]
    old_password = [str(i) for i in old_password]
    old_password = ''.join(old_password)
    return old_password


if __name__ == "__main__":

    cont = True
    # menu option that breaks if option is 3
    while cont:
        menu()
        option = int(input("Please enter an option: "))

        if option == 1:
            user_input = input("Please enter your password to encode: ")
            new_value = encode(user_input)
            print("Your password has been encoded and stored! \n")
        elif option == 2:
            original = decode(new_value)
            print(f"The encoded password is {new_value}, and the original password is {original}\n")
        elif option == 3:
            cont = False
