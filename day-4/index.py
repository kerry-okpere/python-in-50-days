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

value = input("What do you choose? Type 'rock', 'paper' or 'scissors' ").lower()

constants = ["rock", "paper", "scissors"]
computer_choice = random.choice(constants)

if value == "rock" and computer_choice == "rock":
    print(rock)
    print("Computer chose:")
    print(rock)
    print("It's a draw.")
elif value == "rock" and computer_choice == "paper":
    print(rock)
    print("Computer chose:")
    print(paper)
    print("You lose.")
elif value == "rock" and computer_choice == "scissors":
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You win.")
elif value == "paper" and computer_choice == "rock":
    print(paper)
    print("Computer chose:")
    print(rock)
    print("You win.")
elif value == "paper" and computer_choice == "paper":
    print(paper)
    print("Computer chose:")
    print(paper)
    print("It's a draw.")
elif value == "paper" and computer_choice == "scissors":    
    print(paper)
    print("Computer chose:")
    print(scissors)
    print("You lose.")
elif value == "scissors" and computer_choice == "rock":
    print(scissors)
    print("Computer chose:")
    print(rock)
    print("You lose.")
elif value == "scissors" and computer_choice == "paper":
    print(scissors)
    print("Computer chose:")
    print(paper)
    print("You win.")
elif value == "scissors" and computer_choice == "scissors":
    print(scissors)
    print("Computer chose:")
    print(scissors)
    print("It's a draw.")
else:
    print("Invalid input. Game Over.")
