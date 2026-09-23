def greet():
    print("-----Number Parity/Divisibilty Checker-----")

def get_number():
    while True:
        try:
            number = int(input("\nType a number below\n"))
            if type(number) != int:
                raise ValueError
            if number == 0:
                raise ZeroDivisionError
            return number
        except ValueError:
            print("\nERROR: expected an integer\n")
        except ZeroDivisionError:
            print("\nERROR: Division by zero not possible\n")

def check_parity(number):
    print(number % 2 == 0)

def multiple_four(number):
    return number % 4 == 0

def program_loop():
    while True:
        try:
            user_choice = input("\nType c to check another number or q to quit\n")
            if user_choice.lower() == "q" or user_choice.lower() == "quit":
                return False
            elif user_choice.lower() == "c" or user_choice.lower() == "check":
                return True
            else:
                raise ValueError
        except ValueError:
            print("\nERROR: expected c or q\n")

def divide_and_check(numerator, denominator):
    quotient = numerator / denominator
    print(f"\nDividing {numerator} by {denominator}...")
    print(f"Quotient: {round(quotient, 2)}")
    print("Checking divisibility...")
    return numerator % denominator == 0

def path_one():
    print("\nProgram will return True if number is even or False if odd")
    while True:
        user_number = get_number()
        check_parity(user_number)
        if multiple_four(user_number):
            print("Multiple of four detected")
        if program_loop():
            continue
        else:
            print("\nProgram terminating...\nGoodbye")
            break

def path_two():
    while True:
        num1 = get_number()
        print("Numerator accepted")
        num2 = get_number()
        print("Denominator accepted")
        if divide_and_check(num1, num2):
            print("Clean divide detected")
        else:
            print("Not a clean divide")
        if program_loop():
            continue
        else:
            print("Program terminating...\nGoodbye")
            break

def choose_path():
    while True:
        try:
            path = input("\nType 1 to check the parity of a single number\nType 2 to check if two numbers divide cleanly\n")
            if path != "1" and path != "2":
                raise ValueError
            return path
        except ValueError:
            print("\nERROR: expected 1 or 2\n")

def main():
    greet()
    path = choose_path()
    if path == "1":
        path_one()
    if path == "2":
        path_two()

if __name__ == "__main__":
    main()
