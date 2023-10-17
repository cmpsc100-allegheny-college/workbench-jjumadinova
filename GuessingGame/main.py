import random

def above_number(guess: int = 0, number: int = 0) -> bool:
    """Compares guess to number to check if it is higher"""
    return guess > number

def below_number(guess: int = 0, number: int = 0) -> bool:
    """Compares guess to number to check if it is lower"""
    return guess < number

def outside_range(guess: int = 0, low: int = 0, high: int = 1) -> bool:
    return guess > high or guess < low

def main():
    lower_limit = 1
    upper_limit = 10
    number_to_guess = random.randint(lower_limit, upper_limit)
    print(number_to_guess)
    
    guess = input(f"Guess a number between {lower_limit} and {upper_limit}: ")
    
    try:
        guess = int(guess)
    except ValueError:
        print("Your number needs to be an integer.")

    if(isinstance(guess, int)):
        guess = int (guess)

    while (guess != number_to_guess):

        try:
            guess = int(input("Wrong guess. Guess again? "))
            if outside_range(guess, lower_limit, upper_limit):
                print("Your number is outside the range. ")
            # pass
            elif above_number(guess, number_to_guess):
                print("Your number is too high. ")
            elif below_number(guess, number_to_guess):
                print("Your number is too low.")
                # print(isinstance(guess, int))
        except ValueError:
            print("Your number needs to be an integer.")
                
    print("You won!")

if __name__ == "__main__":
    main()