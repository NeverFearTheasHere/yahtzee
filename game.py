import random

class Player():
  def takeTurn(self):
    diceValuesToKeep = []
    numberOfRollsTaken = 0

    while len(diceValuesToKeep) < 5 and numberOfRollsTaken < 3:
      if len(diceValuesToKeep) > 0:
        print(f"After round {numberOfRollsTaken}, so far you have kept these dice: {', '.join(map(str, diceValuesToKeep))}")

      numberOfDiceLeftToRoll = 5 - len(diceValuesToKeep)
      numberOfRollsTaken += 1
      print(f'---- ROUND {numberOfRollsTaken} ----')
      newDiceValues = self.rollDice(numberOfDiceLeftToRoll)
      diceValuesToKeep += self.chooseDiceToKeep(newDiceValues) if numberOfRollsTaken < 3 else newDiceValues

    print(f"Your final dice are: {', '.join(map(str, diceValuesToKeep))}")

  def rollDice(self, numberOfDice):
    diceValues = []
    for i in range(0, numberOfDice):
      diceValues.append(random.randint(1,6))
    print(f"Rolled {numberOfDice} dice and got: {', '.join(map(str, diceValues))}")
    return diceValues
  
  def chooseDiceToKeep(self, diceValues):
    diceValuesToKeep = []

    for value in diceValues:
      userInputIsValid = False
      while not userInputIsValid:
        userInput = input(f"Do you want to keep {value}? (Enter y/n) ").lower()
        userInputIsValid = userInput in {"y", "n"}
        if not userInputIsValid:
          print("Invalid input. Please enter y or n.")
        pass
      shouldKeepValue = userInput.lower() == 'y'
      print(f"OK, {'keeping' if shouldKeepValue else 're-rolling'} the {value}")
      if shouldKeepValue: diceValuesToKeep.append(value)

    return diceValuesToKeep


def main():
  player1 = Player()
  player1.takeTurn()
  # TODO - keep score


if __name__ == "__main__":
  main()