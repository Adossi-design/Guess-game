import random
import time
from datetime import datetime

def open_screen():

    print("  "*20, "\nWELCOME TO THE GUESSING GAME\n")

def guess_game():
    global user_name
    global max_attempt
    number = random.randint(1, 100)
    attempt=0
    start_time = time.time()
    try:
         user_level=int(input("\nChoose your level: 1= Easy 2= Medium 3= Difficult\n>>> "))
    except ValueError as e:
        print(f"Error! {e}")
        guess_game()
    else:
        if user_level == 1:
            print(f"Hi Dear {user_name}! You chose easy level!")
            max_attempt = 10
        elif user_level == 2:
            print(f"Hi Dear {user_name}! You chose medium level!")
            max_attempt = 7
        elif user_level == 3:
            print(f"Hi Dear {user_name}! You chose difficult level!")
            max_attempt = 5
        else:
            print("Choose a number between 1 - 3")
            guess_game()

    while True:

        warning_attempt = max_attempt - attempt - 1
        try:
            user_answer = int(input("\nEnter randomly a number between 1 - 100 of your choice\n>>> "))
        except ValueError as e:
            print(f"Error! {e}")
            print("You are only allowed to enter a number!")
        else:
            if number > user_answer > 0:
                print(
                    f"Oops! The number you got is lower than the right one\n-> You have {warning_attempt} attempt(s) left")
                attempt += 1
            elif number < user_answer < 100:
                print(
                    f"Oops! The number you got is greater than the right one\n-> You have {warning_attempt} attempt(s) left")
                attempt += 1
            elif user_answer == number:
                print(" " * 20, "<< | HERE IS YOUR RESULT | >>\n")
                end_time = time.time()
                taken_time = end_time - start_time
                completing_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Congratulation Dear {user_name}! You got the right answer")
                print(f"Here it is: {number}\nThe number of your failed attempt is: {attempt}")
                print(f"It took you {taken_time:.2f} seconds to get the right answer")
                print(f"Datetime: {completing_datetime}")
                print("Thank for going through the game!")
                play_again()
                break

            else:
                print("Please, Enter a number between 1 - 100")
            warning_attempt = max_attempt - attempt
            if max_attempt == attempt:
                print(f"Oop! You reached the maximum number of attempts.\nYou lost the game\nThe right answer is: {number}")
                play_again()

#Let's create a function play again that will ask the user if he/she wanted to replay the game again orr not
def play_again():
    while True:
        try:
            replay=int(input("\nDo you want to play again? 1= Yes or 2= No\n>>> "))
        except ValueError as e:
            print(f"Error! {e}")
            print("Choose a number between 1 - 2")
        else:
            if replay == 1:
                guess_game()
            elif replay == 2:
                print(
                    f"\nThanks for taking time to go through our game.\nHave a Great day!\nSee you soon Dear {user_name}")
                exit()
            else:
                print("Choose a number between 1 and 2")

open_screen()
user_name=str(input("Enter your name:\n>>> "))
guess_game()