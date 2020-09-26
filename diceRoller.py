import random
import time
def diceNumber():
    file = open("dice.txt", "r")
    readfile = file.read()
    return readfile.split(",")

def rollDice():
    while True:
        number = random.randint(1, 6)
        diceRoll=diceNumber[number-1]
        return diceRoll

def main():
  player1=0
  player2=0

  while True:
    player1 = rollDice()
    player2 = rollDice()
    print("Player 1 Roll: "+ str(player1))
    time.sleep(1)
    print("Player 2 Roll: "+ str(player2))
    time.sleep(1)
    if player1==player2:
      print("You both tied!")
    elif player1>player2:
      print("Player1 won! ")
    else:
      print("Player2 won!")
    break



anotherRoll=True
diceNumber = diceNumber()
while anotherRoll:
    diceRolledNumber=rollDice()
    main()
    anotherRollInput=input("Enter any other key to roll again and \'N' to exit\n").upper()
    if anotherRollInput=="N":
      print('Thank you for playing! Hope to see you again.')
      anotherRoll=False

