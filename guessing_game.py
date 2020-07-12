import random

# Game setup
print("Welcome to the Guessing Game")
number_of_guesses = 3
user_won = False

# Computer gets a ransom number between 1 and 10
correct_answer = random.randint(1, 10)
# print(correct_answer)

while number_of_guesses > 0:
    # User guesses the number
    user_guess = input("Guess my number: ")
    user_guess = int(user_guess)

    # Computer gives feedback
    if user_guess == correct_answer:
        print("Good guess... You are correct!")
        user_won = True
        break
    elif user_guess > correct_answer:
        print("Sorry, you guessed too high!")
    elif user_guess < correct_answer:
        print("Sorry, you guessed too low!")

    number_of_guesses -= 1

if user_won:
    print("You Win!")
else:
    print("You Lost!")
