def menu():
    print("Menu")
    print("------------- ")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit \n")


def encode(value):
    new_value = ""

    for char in value:
        encoded_value = str((int(char) + 3) % 10)
        new_value += encoded_value
    return new_value


def decode(new_value):
    original_value = ""

    for char in new_value:
        encoded_value = str((int(char) - 3) % 10)
        original_value += encoded_value
    return original_value


if __name__ == "__main__":

    cont = True

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
