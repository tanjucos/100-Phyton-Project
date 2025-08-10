import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



selection = ["Rock", "Paper", "Scissors"]
selection = ["0","1","2"]

possibility1 = ["Rock", "Scissors"]
possibility2 = ["Scissors", "Rock"]
possibility3 = ["Paper", "Scissors"]
possibility4 = ["Scissors", "Paper"]
possibility5 = ["Rock", "Paper"]
possibility6 = ["Paper", "Rock"]
possibiltiy7 = ["Rock", "Rock"]
possibiltiy8 = ["Paper", "Paper"]
possibiltiy9 = ["Scissors", "Scissors"]

possibility1 = ["0", "2"] #Computer Wins - Game Over!
possibility2 = ["2", "0"] #You Won!
possibility3 = ["1", "2"] #You Won!
possibility4 = ["2", "1"] #Computer Wins - Game Over!
possibility5 = ["0", "1"] #You Won!
possibility6 = ["1", "0"] #Computer Wins - Game Over!
possibiltiy7 = ["0", "0"] #Even! Try it again!
possibiltiy8 = ["1", "1"] #Even! Try it again!
possibiltiy9 = ["2", "2"] #Even! Try it again!

game_images = [rock, paper, scissors]

choice1 = random.choice(selection)
print(choice1)

choice2 = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors").strip().upper()

if choice2 == "0":
    print("Rock")
elif choice2 == "1":
    print("Paper")
else:
    print("Scissors")

verdict = [choice1, choice2]

if verdict == possibility1:
    print("Computer Wins! - Game Over")
elif verdict == possibility2:
    print("You Won! - Congrats!")
elif verdict == possibility3:
    print("You Won! - Congrats!")
elif verdict == possibility4:
    print("Computer Wins! - Game Over")
elif verdict == possibility5:
    print("You Won! - Congrats!")
elif verdict == possibility6:
    print("Computer Wins! - Game Over")
elif verdict == possibiltiy7:
    print("Even- Try it Again!")
elif verdict == possibiltiy8:
    print("Even- Try it Again!")
else:
    print("Even- Try it Again!")


# Code is not great, will be enhanced!