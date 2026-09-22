def prompt():
    name = input("What is your name?\n")
    while True:
        age = input("What is your age?\n")
        if int(age) <= 0:
            print("Age cannot be zero or less.")
        else:
            break
    year = input("What year is it?\n")
    return name, int(age), int(year)

user_name, user_age, current_year = prompt()

def calculate_year(): # returns year the user will turn 100
    years_until = 100 - user_age
    return current_year + years_until

def main():
    print(f"You ({user_name}) were born in {current_year - user_age} and will turn 100 in the year {calculate_year()}")

if __name__ == "__main__":
    main()
