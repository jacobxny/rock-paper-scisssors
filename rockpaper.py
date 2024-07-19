import random 

choice = str(input("Rock, Paper or Scissors? "))

if choice == "rock":
    choice = 1
elif choice == "paper":
    choice = 2
elif choice == "scissors":
    choice = 3
else:
    print("Invalid try again.")

choice2 = random.randint(1, 3)

if choice == choice2:
    print("Draw. ")
if choice == 1:
    if choice2 == 2:
        print("You Lose. Since rock loses to paper. :( ")
if choice == 2:
    if choice2 == 1:
        print("You Win. Since paper beats rock. :) ")
if choice == 3:
    if choice2 == 2:
        print("You Win. Since scissors beats paper. :) ")
if choice == 2:
    if choice2 == 3:
        print("You Lose. Since paper loses to scissors. :( ")
if choice == 3:
    if choice2 == 1:
        print("You Lose. Since scissors loses to rock. :( ")
if choice == 1:
    if choice2 == 3:
        print("You Win. Since rock beats scissors :)")
