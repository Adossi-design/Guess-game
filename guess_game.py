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
    user_level=int(input("\nChoose your level: 1= Easy 2= Medium 3= Difficult\n>>> "))
    if user_level == 1:
        print(f"Hi Dear {user_name}! You chose easy level!")
        max_attempt = 10
    elif user_level == 2:
        print(f"Hi Dear {user_name}! You chose medium level!")
        max_attempt = 7
    elif user_level ==3:
        print(f"Hi Dear {user_name}! You chose difficulty level!")
        max_attempt=5
    else:
        print("Choose a number between 1 - 3")
        guess_game()

    while True:

        user_answer = int(input("\nEnter randomly one number in your choice\n>>> "))
        warning_attempt = max_attempt - attempt -1
        if number > user_answer:
            print(f"Oops! The number you got is lower than the right one\n-> You have {warning_attempt} left")
            attempt += 1
        elif number < user_answer:
            print(f"Oops! The number you got is greater than the right one\n-> You have {warning_attempt} left")
            attempt += 1
        else:
            print(" "*20, "<< | HERE IS YOUR RESULT | >>\n")
            end_time = time.time()
            taken_time = end_time - start_time
            completing_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Congratulation Dear {user_name}! You got the right")
            print(f"Here it is: {number}\nThe number of your failed attempt is: {attempt}")
            print(f"It took you {taken_time} seconds to get the right answer")
            print(f"Datetime: {completing_datetime}")
            print("Thank for going through the game!")
            break
        warning_attempt = max_attempt - attempt
        if max_attempt == attempt:
            print(f"Oop! You reached the maximum number of attempts.\nYou lost the game\nThe right answer is: {number}")
            play_again()
#Let's create a function play again that will ask the user if he/she wanted to replay the game again orr not
def play_again():
    while True:
         replay=int(input("\nDo you want to play again? 1= Yes or 2= No\n>>> "))
         if replay == 1:
              guess_game()
         elif replay == 2:
              print(f"\nThanks for taking time to go through our game.\nHave a Great day!\nSee you soon Dear {user_name}")
              exit()
         else:
               print("Choose a number between 1 and 2")

open_screen()
user_name=input("Enter your name:\n>>> ")
guess_game()