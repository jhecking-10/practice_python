# Ask user for a number, then 
# check to see if it's odd or even

def greet():
    print("-----Odd or Even Number Checker-----")
    print("Program will return True if number is even and False if odd")

def get_number():
    while True:
        try:
            number = int(input("Type any number below\n"))
            if type(number) != int:
                raise ValueError
            return number
        except ValueError:
            print("Please provide an integer")

def check(number):
    print(number % 2 == 0)

def multiple_four(number):
    return number % 4 == 0

def program_loop():
    while True:
        try:
            user_choice = input("Type C to check another number or Q to quit\n")
            if user_choice.lower() == "q":
                return False
            elif user_choice.lower() == "c":
                return True
            else:
                raise ValueError
        except ValueError:
            print("Type c or q")

def main():
    greet()
    while True:
        user_number = get_number()
        check(user_number)
        if multiple_four(user_number):
            print("Multiple of four detected")
        if program_loop():
            continue
        else:
            print("Program terminating...\nGoodbye")
            break

if __name__ == "__main__":
    main()
