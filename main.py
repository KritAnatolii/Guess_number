from random import randint

print('Hello! Welcome to the game \n"Guess the number!"\nGood luck!.')
max_attempt = int(input("Enter the number of attempts: "))
min = int(input("Enter the minimum number: "))
max = int(input("Enter the maximum number: "))
print(f"You have {max_attempt} attempts to guess a number from {min} to {max}.")

secret_number = randint(min, max)
attempt = 1
while attempt <= max_attempt:
    print(f"\nAttempt {attempt} of {max_attempt}")
    try:
        guess = int(input("Your guess: "))
        if min <= guess <= max:
            if guess == secret_number:
                print(f"Congratulations! You guessed it right. The number was {secret_number}")
                break
            if guess < secret_number:
                print("Too low!")
                attempt +=1
            else:
                print("Too high!")
                attempt+=1
        else:
            print(f"Number must be between {min} and {max}.")
    except:
        print("Invalid input. Please enter a whole number.")

else:
    print(f"\nYou used all attempts. The number was {secret_number}.")
