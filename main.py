import random

rock = 1
paper = 2
scissors = 3


choice = random.randint(1,3)

usr = input("Rock, Paper or Scissors: ").lower()


if choice == rock:
  choice = "Rock"
  print("Rock")
  
  if usr == "rock":
    print("It's a tie!")
  elif usr == "paper":
    print("You win!")
  elif usr == "scissors":
    print("I win!")


# paper
elif choice == paper:
  choice = "Paper"
  print("Paper")
  if usr == "rock":
    print("I win!")
  elif usr == "paper":
    print("It's a tie!")
  elif usr == "scissors":
    print("You win!")
     
# scissors
elif choice == scissors:
  
  choice = "Scissors"
  print("Scissors")
  if usr == "rock":
    print("You win!")
  elif usr == "paper":
    print("I win!")
  elif usr == "scissors":
    print("It's a tie!")
