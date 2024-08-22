import random

def guess_number():
    # The computer draws a number from 1 to 100
    random_number = random.randint(1, 100)
    
    # Initialize the variable that stores the user's response
    proposal = None
    
    print("Guess the number from 1 to 100")
    
    # User guessing the number
    while proposal != random_number:
        
        # User proposal
        proposal = int(input("Enter your guess: "))
        
        # Checking if proposal is lower, higher or equal of random number
        if proposal < random_number:
            print("Too low. Try again")
        elif proposal > random_number:
            print("Too high. Try again")
        else:
            print("Congratulations. U guessed the number")

# Run the game
guess_number()
