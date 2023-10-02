import random

def above_number(guess: int = 0, number: int = 0) -> bool:
    """Compares guess to number to check if it is higher"""
    return guess > number

def below_number(guess: int = 0, number: int = 0) -> bool:
    """Compares guess to number to check if it is lower"""
    return guess < number

def main():
    lower_limit = 1
    upper_limit = 10
    number_to_guess = random.randint(lower_limit, upper_limit)
    # print(number_to_guess)
    guess = int(input(f"Guess a number between {lower_limit} and {upper_limit}: "))

    while(guess != number_to_guess):
        guess = int(input("Wrong guess. Guess again?"))
        if above_number(guess, number_to_guess):
            print("Your number is too high")
        elif below_number(guess, number_to_guess):
            print("Your number is too low")

    print("You won!")

if __name__ == "__main__":
    main()