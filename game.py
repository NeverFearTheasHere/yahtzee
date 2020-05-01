import random
import enum


class Scores(enum.Enum):
  Yahtzee = 1
  FourOfAKind = 2
  ThreeOfAKind = 3
  Nothing = 4


class Player():
  diceValuesToKeep = []

  def takeTurn(self):
    self.diceValuesToKeep = []
    numberOfRollsTaken = 0

    while len(self.diceValuesToKeep) < 5 and numberOfRollsTaken < 3:
      if len(self.diceValuesToKeep) > 0:
        print(f"After round {numberOfRollsTaken}, so far you have kept these dice: {', '.join(map(str, self.diceValuesToKeep))}")

      numberOfDiceLeftToRoll = 5 - len(self.diceValuesToKeep)
      numberOfRollsTaken += 1
      print(f'---- ROUND {numberOfRollsTaken} ----')
      newDiceValues = self.diceValuesToKeep + self.rollDice(numberOfDiceLeftToRoll)

      if numberOfRollsTaken < 3:
        self.chooseDiceToKeep(newDiceValues) 
      else:
        self.diceValuesToKeep = newDiceValues

    print(f"Your final dice are: {', '.join(map(str, self.diceValuesToKeep))}")

  def rollDice(self, numberOfDice):
    diceValues = []
    for i in range(0, numberOfDice):
      diceValues.append(random.randint(1,6))
    print(f"Rolled {numberOfDice} dice and got: {', '.join(map(str, diceValues))}")
    return diceValues
  
  def chooseDiceToKeep(self, diceValues):
    print(f"Your dice now are: {', '.join(map(str, diceValues))}")

    self.diceValuesToKeep = []

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
      if shouldKeepValue: self.diceValuesToKeep.append(value)

  def calculateScore(self):
    ones = list(filter(lambda x: x == 1, self.diceValuesToKeep))
    twos = list(filter(lambda x: x == 2, self.diceValuesToKeep))
    threes = list(filter(lambda x: x == 3, self.diceValuesToKeep))
    fours = list(filter(lambda x: x == 4, self.diceValuesToKeep))
    fives = list(filter(lambda x: x == 5, self.diceValuesToKeep))
    sixes = list(filter(lambda x: x == 6, self.diceValuesToKeep))

    maxNumberOfAKind = max([len(ones), len(twos), len(threes), len(fours), len(fives), len(sixes)])
    
    if maxNumberOfAKind == 5:
      return Scores['Yahtzee']

    if maxNumberOfAKind == 4:
      return Scores['FourOfAKind']

    if maxNumberOfAKind == 3:
      return Scores['ThreeOfAKind']

    return Scores['Nothing']


def main():
  player1 = Player()
  player1.takeTurn()
  score = player1.calculateScore()

  if score == Scores['Yahtzee']:
    print(f"You scored a yahtzee (five of a kind)!")

  elif score == Scores['FourOfAKind']:
    print(f"You scored four of a kind!")

  elif score == Scores['ThreeOfAKind']:
    print(f"You scored three of a kind!")

  else:
    print(f"You didn't score anything")


if __name__ == "__main__":
  main()