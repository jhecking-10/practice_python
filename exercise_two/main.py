# Ask user for a number, then check to see if it's odd or even

def greet():
    print("-----Odd or Even Number Checker-----")
    print("Program will return True if number is even and False if odd")

def get_number():
    return int(input("Type any number below\n"))

def check(number: int):
    print(number % 2 == 0)

def main():
    greet()
    num = get_number()
    check(num)

main()
