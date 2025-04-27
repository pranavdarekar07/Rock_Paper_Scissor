import random

print("Game - Rock-Paper-Scissor")

#list
game = ["rock","paper","scissor"]

#for while loop
i=0
user_score = 0
computer_score = 0

#while loop for continue looping
while i < 5:

    #random selection from list
    computer_choice = random.choice(game)

    #user input value
    user = input("(Rock,Paper,Scissor) : ").lower().replace(" ","")
    if user in game:
        if user == computer_choice:
            print("tie")
            print("------------------------------------------------------------------------------------")
        elif user == "rock" and computer_choice == "paper":
            print("This Round computer win !!!")
            computer_score += 1
            print("------------------------------------------------------------------------------------")
        elif user == "paper" and computer_choice == "scissor":
            print("This Round computer win !!!")
            computer_score += 1
            print("------------------------------------------------------------------------------------")
        elif user == "scissor" and computer_choice == "rock":
            print("This Round computer win !!!")
            computer_score += 1
            print("------------------------------------------------------------------------------------")
        else:
            print("This round User win !!!")
            user_score += 1
            print("------------------------------------------------------------------------------------")
    else:
        print("Please Type valid input!!!")
        i -= 1
    i += 1

#socre
if user_score < computer_score:
    print(f"Computer wins the game by {computer_score} points")
elif user_score == computer_score:
    print(f"Computer and User tie...")
else:
    print(f"User wins the game by {user_score} points")