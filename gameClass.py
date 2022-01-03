

"""
Analysis:

Problem: A Tic-Tac-Toe game a user can play and reset at will. 

Output to monitor:
  None
  

Input from keyboard:
  None

CONSTANTS:

  WINNING_COMBOS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],
                    [3 ,6, 9], [1, 5, 9], [3, 5, 7]]
  POSSIBLE_SETS = ["O", "X", "---"]
  ZERO_CONSTANT = 0
  BOX_ONE = 1
  BOX_TWO = 2
  BOX_THREE = 3
  BOX_FOUR = 4
  BOX_FIVE = 5
  BOX_SIX = 6
  BOX_SEVEN = 7
  BOX_EIGHT = 8
  BOX_NINE = 9
  BOX_NUMBER = [BOX_ONE, BOX_TWO, BOX_THREE, BOX_FOUR, BOX_FIVE, BOX_SIX,
                BOX_SEVEN, BOX_EIGHT, BOX_NINE]

Tasks allocated to functions:

  class - Game: Game logic for Tic-Tac-Toe game
    __init__(self) - constructor for gameGUI
    winnerTestX(self) - predicate function that tests if player has won
    winnerTestO(self) - predicate function that tests if the computer has won
    getXList(self) - returns the xList
    getOList(self) - returns the oList
    addToList(self, aStr, index)(str, int) - takes in an index for WINNING_COMBOS
      and aStr to take part in Boolian check for X or O. addes the box number to
      either X or O list
    
"""    

#Create Logic Class (Matthew Fay) -------------------------------------


class Game:
  #Constants
  WINNING_COMBOS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],
                    [3 ,6, 9], [1, 5, 9], [3, 5, 7]]
  POSSIBLE_SETS = ["O", "X", "---"]

  ZERO_CONSTANT = 0
  
  BOX_ONE = 1

  BOX_TWO = 2

  BOX_THREE = 3

  BOX_FOUR = 4

  BOX_FIVE = 5

  BOX_SIX = 6

  BOX_SEVEN = 7

  BOX_EIGHT = 8

  BOX_NINE = 9

  BOX_NUMBER = [BOX_ONE, BOX_TWO, BOX_THREE, BOX_FOUR, BOX_FIVE, BOX_SIX,
                BOX_SEVEN, BOX_EIGHT, BOX_NINE]
  
  #Constructor ---------------------------------------------------------
  def __init__(self):
    self.__xList = []
    self.__oList = []
    ##self.__theMode = input("Imput 1 for test Mode, Enter for Regular Mode: ")


  #Failed implemenation of Game Mode function
  ''' 
  def makeMove(self, takenBoxes):
    if self.__theMode:
      theMove = random.seed(a = SEED, version = 2)
      theMove = random.randrange(0, 9)
    while theMove in takenBoxes:
      theMove = random.randrange(0, 9)
    return theMove
  '''

  
  #Predicates (Vincent Preikstas) ------------------------------------------------------
  def winnerTestX(self): 
    for item in self.WINNING_COMBOS:
      if item[0] in self.__xList and item[1] in self.__xList and item[self.BOX_TWO] in self.__xList:
        return True
      else:
        winning = False

    return winning
  def winnerTestO(self):
    for item in self.WINNING_COMBOS:
      if item[0] in self.__oList and item[1] in self.__oList and item[self.BOX_TWO] in self.__oList:
        return True
      else:
        winning = False

    return winning
  
  #Alternate Version of winner test. Couldnt get it to work without two returns
  
  '''def winnerTest(self, aList): ####
    result = False
    while result == False:
      for item in self.WINNING_COMBOS:
        if item[0] in aList and item[1] in aList and item[2] in aList:
         result = True

    return result
  '''

  
  #Accessors --------------------------------------------------------------
  
  def getXList(self):
    return self.__xList

  def getOList(self):
    return self.__oList

  #Mutators (Matthew Fay) ---------------------------------------------------
  
  def addToList(self, aStr, index):
    if aStr == 'X':
      number = self.BOX_NUMBER[index]
      ##print(self.__xList)
      self.__xList += [number]
      ##print(self.__xList)
      ##result = self.winnerTest(self.__xList)
      ##print(result)
    else:
      number = self.BOX_NUMBER[index]
      self.__oList += [number]
    
  def reset(self):
    self.__xList = []
    self.__oList = []




##newGame = Game()
##newGame.addToList('X', 0)
  
  
