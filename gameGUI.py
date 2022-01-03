

"""
Analysis:

Problem: A Tic-Tac-Toe gameGUI a user can play and reset at will. 

Output to monitor:
  gameGUI- User interface
  

Input from keyboard:
  None

CONSTANTS:

  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  NINE = 9
  EIGHT = 8
  
  BOX_ONE = 0
  BOX_TWO = 1
  BOX_THREE = 2
  BOX_FOUR = 3
  BOX_FIVE = 4
  BOX_SIX = 5
  BOX_SEVEN = 6
  BOX_EIGHT = 7
  BOX_NINE = 8

  SEED = 1

Tasks allocated to functions:

  class - gameGUI: GUI for the Tic-Tac-Toe game
    __init__(self) - constructor for gameGUI
    resetButtonHandler(self) - resets the gui and game values back to initial
      values
    testModeHandler(self) - sets the game mode to test mode
    regularModeHandler(self) - set the game mode to regular mode
    recordBoxes(self, boxNumber) - takes in a box number and appends that to the list
      of used boxes
    userRowFunctions(self) - Nine similar functions that handle player moves and
      invoke computer move
"""    


#Importing files-----------------------------------------------------------
import random
from tkinter import *
from gameClass import *

##import tkFont
##theMode = input("Imput 1 for test Mode, Enter for Regular Mode: ")



#Creating GUI class (Vincent Preikstas)-----------------------------------------------


class gameGUI:
  #CONSTANTS
  
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  NINE = 9
  EIGHT = 8
  
  BOX_ONE = 0
  BOX_TWO = 1
  BOX_THREE = 2
  BOX_FOUR = 3
  BOX_FIVE = 4
  BOX_SIX = 5
  BOX_SEVEN = 6
  BOX_EIGHT = 7
  BOX_NINE = 8

  SEED = 1
  def __init__(self):
    ##self.__theMode = input("God Damn It: ")
    self.__takenBoxes = []
    self.__startGame = Game()
    self.__gameMode = ''
    self.__window = Tk()
    ##self.__window.grid()

    #Dynamic Label variable------------
    self.__instructions = StringVar('','X Starts: Choose a square', '')
    ##instructions = 'X Starts: Choose any square'
    
    #Labels----------------------------
    self.__gameLabel = Label(self.__window, text = "TicTacToe!")
    self.__gameLabel.grid(row = 0, column = 1)
    self.__instructionsLabel = Label(self.__window, textvariable = self.__instructions)
    self.__instructionsLabel.grid(row = 1, column = 1)


    #InterfaceButtons----------------------------------
    
    self.__exitButton = Button(self.__window, text = "Exit",
                               command = self.__window.destroy)
    self.__exitButton.grid(row = 1, column = 0)
    self.__resetButton = Button (self.__window, text = "Reset",
                                 command = self.resetButtonHandler)
    self.__resetButton.grid(row = 1, column = self.TWO)
    self.__testModeButton = Button(self.__window, text = "Test Mode",
                                   command = self.testModeHandler)
    self.__testModeButton.grid(row = self.FIVE, column = self.TWO)

    self.__regularModeButton = Button(self.__window, text = "Regular Mode",
                                      command = self.regularModeHandler)
    self.__regularModeButton.grid(row = self.FIVE, column = 0)
    

    #GameButtons (Matthew Fay)------------------------------------------
    
    
    self.__row2Column0Button = Button(self.__window, text = '---', font = 'Arial 40 bold',
                                      command = self.userRow2Column0ButtonEH)
    self.__row2Column0Button.grid(row = self.TWO, column = 0)

    self.__row3Column0Button = Button(self.__window, text = '---',
                                      command = self.userRow3Column0ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row3Column0Button.grid(row = self.THREE, column = 0)

    self.__row4Column0Button = Button(self.__window, text = '---',
                                      command = self.userRow4Column0ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row4Column0Button.grid(row = self.FOUR, column = 0)
    
    self.__row2Column1Button = Button(self.__window, text = '---',
                                      command = self.userRow2Column1ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row2Column1Button.grid(row = self.TWO, column = 1)

    self.__row3Column1Button = Button(self.__window, text = '---',
                                      command = self.userRow3Column1ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row3Column1Button.grid(row = self.THREE, column = 1)

    self.__row4Column1Button = Button(self.__window, text = '---',
                                      command = self.userRow4Column1ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row4Column1Button.grid(row = self.FOUR, column = 1)

    self.__row2Column2Button = Button(self.__window, text = '---',
                                      command = self.userRow2Column2ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row2Column2Button.grid(row = self.TWO, column = self.TWO)

    self.__row3Column2Button = Button(self.__window, text = '---',
                                      command = self.userRow3Column2ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row3Column2Button.grid(row = self.THREE, column = self.TWO)

    self.__row4Column2Button = Button(self.__window, text = '---',
                                     command = self.userRow4Column2ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row4Column2Button.grid(row = self.FOUR, column = self.TWO)
    
    mainloop()


  #Event Handlers (Vincent Preikstas + Matthew Fay)--------------------------------  

  
  def resetButtonHandler(self):
    self.__startGame = Game()
    self.__takenBoxes = []
    self.__instructions.set ('X Starts: Choose a square')


    self.__blankLabelOne = Label(self.__window, text = '---', font = 'Arial 40 bold')
    self.__blankLabelOne.grid(row = self.TWO, column = 0)

    self.__blankLabelTwo = Label(self.__window, text = '---', font = 'Arial 40 bold')
    self.__blankLabelTwo.grid(row = self.THREE, column = 0)

    self.__blankLabelThree = Label(self.__window, text = '---', font = 'Arial 40 bold')
    self.__blankLabelThree.grid(row = self.FOUR, column = 0)

    self.__blankLabelFour = Label(self.__window, text = '---', font = 'Arial 40 bold')
    self.__blankLabelFour.grid(row = self.TWO, column = 1)

    self.__blankLabelFive = Label(self.__window, text = '---', font = 'Arial 40 bold')
    self.__blankLabelFive.grid(row = self.THREE, column = 1)

    self.__blankLabelSix = Label(self.__window, text = '---', font = 'Arial 40 bold')
    self.__blankLabelSix.grid(row = self.FOUR, column = 1)

    self.__blankLabelSeven = Label(self.__window, text = '---', font = 'Arial 40 bold')
    self.__blankLabelSeven.grid(row = self.TWO, column = self.TWO)

    self.__blankLabelEight = Label(self.__window, text = '---', font = 'Arial 40 bold')
    self.__blankLabelEight.grid(row = self.THREE, column = self.TWO)

    self.__blankLabelNine = Label(self.__window, text = '---', font = 'Arial 40 bold')
    self.__blankLabelNine.grid(row = self.FOUR, column = self.TWO)
    
    self.__row2Column0Button = Button(self.__window, text = '---', font = 'Arial 40 bold',
                                      command = self.userRow2Column0ButtonEH)
    self.__row2Column0Button.grid(row = self.TWO, column = 0)

    self.__row3Column0Button = Button(self.__window, text = '---',
                                      command = self.userRow3Column0ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row3Column0Button.grid(row = self.THREE, column = 0)

    self.__row4Column0Button = Button(self.__window, text = '---',
                                      command = self.userRow4Column0ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row4Column0Button.grid(row = self.FOUR, column = 0)
    
    self.__row2Column1Button = Button(self.__window, text = '---',
                                      command = self.userRow2Column1ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row2Column1Button.grid(row = self.TWO, column = 1)

    self.__row3Column1Button = Button(self.__window, text = '---',
                                      command = self.userRow3Column1ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row3Column1Button.grid(row = self.THREE, column = 1)

    self.__row4Column1Button = Button(self.__window, text = '---',
                                      command = self.userRow4Column1ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row4Column1Button.grid(row = self.FOUR, column = 1)

    self.__row2Column2Button = Button(self.__window, text = '---',
                                      command = self.userRow2Column2ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row2Column2Button.grid(row = self.TWO, column = self.TWO)

    self.__row3Column2Button = Button(self.__window, text = '---',
                                      command = self.userRow3Column2ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row3Column2Button.grid(row = self.THREE, column = self.TWO)

    self.__row4Column2Button = Button(self.__window, text = '---',
                                     command = self.userRow4Column2ButtonEH,
                                      font = 'Arial 40 bold')
    self.__row4Column2Button.grid(row = self.FOUR, column = self.TWO)
    
  def testModeHandler(self):
    self.__gameMode = '1'

  def regularModeHandler(self):
    self.__gameMode = ''

  def recordBoxes (self, boxNumber):
    self.__takenBoxes.append(boxNumber)
    ##print(self.__takenBoxes)


  def doMove(self):
    ##theMove = self.__startGame.makeMove(self.__takenBoxes)
    if self.__gameMode:
      theMove = random.seed(a = self.SEED, version = self.TWO)
    theMove = random.randrange(0, self.NINE)
    while theMove in self.__takenBoxes:
      theMove = random.randrange(0, self.NINE)
      
    if theMove == self.BOX_ONE:
      compMove = 'O'
      self.__newLabel = Label(self.__window, text = 'O', font = 'Arial 50 bold')
      self.__newLabel.grid(row = self.TWO, column = 0)
      self.__startGame.addToList(compMove, self.BOX_ONE)
      self.__row2Column0Button.grid_forget()
      self.recordBoxes(self.BOX_ONE)
      if self.__startGame.winnerTestO():
        self.__instructions.set("You Lose!!!")
        self.__row2Column0Button.grid_forget()
        self.__row3Column0Button.grid_forget()
        self.__row4Column0Button.grid_forget()
        self.__row2Column1Button.grid_forget()
        self.__row3Column1Button.grid_forget()
        self.__row4Column1Button.grid_forget()
        self.__row2Column2Button.grid_forget()
        self.__row3Column2Button.grid_forget()
        self.__row4Column2Button.grid_forget()
    elif theMove == self.BOX_FOUR:
      compMove = 'O'
      self.__newLabel = Label(self.__window, text = 'O', font = 'Arial 50 bold')
      self.__newLabel.grid(row = self.THREE, column = 0)
      self.__startGame.addToList(compMove, self.BOX_FOUR)
      self.__row3Column0Button.grid_forget()
      self.recordBoxes(self.BOX_FOUR)
      if self.__startGame.winnerTestO():
        self.__instructions.set("You Lose!!!")
        self.__row2Column0Button.grid_forget()
        self.__row3Column0Button.grid_forget()
        self.__row4Column0Button.grid_forget()
        self.__row2Column1Button.grid_forget()
        self.__row3Column1Button.grid_forget()
        self.__row4Column1Button.grid_forget()
        self.__row2Column2Button.grid_forget()
        self.__row3Column2Button.grid_forget()
        self.__row4Column2Button.grid_forget()
    elif theMove == self.BOX_SEVEN:
      compMove = 'O'
      self.__newLabel = Label(self.__window, text = 'O', font = 'Arial 50 bold')
      self.__newLabel.grid(row = self.FOUR, column = 0)
      self.__startGame.addToList(compMove, self.BOX_SEVEN)
      self.__row4Column0Button.grid_forget()
      self.recordBoxes(self.BOX_SEVEN)
      if self.__startGame.winnerTestO():
        self.__instructions.set("You Lose!!!")
        self.__row2Column0Button.grid_forget()
        self.__row3Column0Button.grid_forget()
        self.__row4Column0Button.grid_forget()
        self.__row2Column1Button.grid_forget()
        self.__row3Column1Button.grid_forget()
        self.__row4Column1Button.grid_forget()
        self.__row2Column2Button.grid_forget()
        self.__row3Column2Button.grid_forget()
        self.__row4Column2Button.grid_forget()
    elif theMove == self.BOX_TWO:
      compMove = 'O'
      self.__newLabel = Label(self.__window, text = 'O', font = 'Arial 50 bold')
      self.__newLabel.grid(row = self.TWO, column = 1)
      self.__startGame.addToList(compMove, self.BOX_TWO)
      self.__row2Column1Button.grid_forget()
      self.recordBoxes(self.BOX_TWO)
      if self.__startGame.winnerTestO():
        self.__instructions.set("You Lose!!!")
        self.__row2Column0Button.grid_forget()
        self.__row3Column0Button.grid_forget()
        self.__row4Column0Button.grid_forget()
        self.__row2Column1Button.grid_forget()
        self.__row3Column1Button.grid_forget()
        self.__row4Column1Button.grid_forget()
        self.__row2Column2Button.grid_forget()
        self.__row3Column2Button.grid_forget()
        self.__row4Column2Button.grid_forget()
    elif theMove == self.BOX_FIVE:
      compMove = 'O'
      self.__newLabel = Label(self.__window, text = 'O', font = 'Arial 50 bold')
      self.__newLabel.grid(row = self.THREE, column = 1)
      self.__startGame.addToList(compMove, self.BOX_FIVE)
      self.__row3Column1Button.grid_forget()
      self.recordBoxes(self.BOX_FIVE)
      if self.__startGame.winnerTestO():
        self.__instructions.set("You Lose!!!")
        self.__row2Column0Button.grid_forget()
        self.__row3Column0Button.grid_forget()
        self.__row4Column0Button.grid_forget()
        self.__row2Column1Button.grid_forget()
        self.__row3Column1Button.grid_forget()
        self.__row4Column1Button.grid_forget()
        self.__row2Column2Button.grid_forget()
        self.__row3Column2Button.grid_forget()
        self.__row4Column2Button.grid_forget()
    elif theMove == self.BOX_EIGHT:
      compMove = 'O'
      self.__newLabel = Label(self.__window, text = 'O', font = 'Arial 50 bold')
      self.__newLabel.grid(row = self.FOUR, column = 1)
      self.__startGame.addToList(compMove, self.BOX_EIGHT)
      self.__row4Column1Button.grid_forget()
      self.recordBoxes(self.BOX_EIGHT)
      if self.__startGame.winnerTestO():
        self.__instructions.set("You Lose!!!")
        self.__row2Column0Button.grid_forget()
        self.__row3Column0Button.grid_forget()
        self.__row4Column0Button.grid_forget()
        self.__row2Column1Button.grid_forget()
        self.__row3Column1Button.grid_forget()
        self.__row4Column1Button.grid_forget()
        self.__row2Column2Button.grid_forget()
        self.__row3Column2Button.grid_forget()
        self.__row4Column2Button.grid_forget()
    elif theMove == self.BOX_THREE:
      compMove = 'O'
      self.__newLabel = Label(self.__window, text = 'O', font = 'Arial 50 bold')
      self.__newLabel.grid(row = self.TWO, column = self.TWO)
      self.__startGame.addToList(compMove, self.BOX_THREE)
      self.__row2Column2Button.grid_forget()
      self.recordBoxes(self.BOX_THREE)
      if self.__startGame.winnerTestO():
        self.__instructions.set("You Lose!!!")
        self.__row2Column0Button.grid_forget()
        self.__row3Column0Button.grid_forget()
        self.__row4Column0Button.grid_forget()
        self.__row2Column1Button.grid_forget()
        self.__row3Column1Button.grid_forget()
        self.__row4Column1Button.grid_forget()
        self.__row2Column2Button.grid_forget()
        self.__row3Column2Button.grid_forget()
        self.__row4Column2Button.grid_forget()
    elif theMove == self.BOX_SIX:
      compMove = 'O'
      self.__newLabel = Label(self.__window, text = 'O', font = 'Arial 50 bold')
      self.__newLabel.grid(row = self.THREE, column = self.TWO)
      self.__startGame.addToList(compMove, self.BOX_SIX)
      self.__row3Column2Button.grid_forget()
      self.recordBoxes(self.BOX_SIX)
      if self.__startGame.winnerTestO():
        self.__instructions.set("You Lose!!!")
        self.__row2Column0Button.grid_forget()
        self.__row3Column0Button.grid_forget()
        self.__row4Column0Button.grid_forget()
        self.__row2Column1Button.grid_forget()
        self.__row3Column1Button.grid_forget()
        self.__row4Column1Button.grid_forget()
        self.__row2Column2Button.grid_forget()
        self.__row3Column2Button.grid_forget()
        self.__row4Column2Button.grid_forget()
    else:
      compMove = 'O'
      self.__newLabel = Label(self.__window, text = 'O', font = 'Arial 50 bold')
      self.__newLabel.grid(row = self.FOUR, column = self.TWO)
      self.__startGame.addToList(compMove, self.BOX_NINE)
      self.__row4Column2Button.grid_forget()
      self.recordBoxes(self.BOX_NINE)
      if self.__startGame.winnerTestO():
        self.__instructions.set("You Lose!!!")
        self.__row2Column0Button.grid_forget()
        self.__row3Column0Button.grid_forget()
        self.__row4Column0Button.grid_forget()
        self.__row2Column1Button.grid_forget()
        self.__row3Column1Button.grid_forget()
        self.__row4Column1Button.grid_forget()
        self.__row2Column2Button.grid_forget()
        self.__row3Column2Button.grid_forget()
        self.__row4Column2Button.grid_forget()

  #Game Button EH (Matthew Fay)-----------------------------------      
 
  def userRow2Column0ButtonEH(self):
    userInput = 'X'
    self.__row2Column0LabelX = Label(self.__window, text = 'X', font = 'Arial 50 bold')
    self.__row2Column0LabelX.grid(row = self.TWO, column = 0)
    self.__startGame.addToList(userInput, self.BOX_ONE)
    self.__row2Column0Button.grid_forget()
    self.recordBoxes(self.BOX_ONE)
    if self.__startGame.winnerTestX():
      self.__instructions.set("You Win!")
      self.__row2Column0Button.grid_forget()
      self.__row3Column0Button.grid_forget()
      self.__row4Column0Button.grid_forget()
      self.__row2Column1Button.grid_forget()
      self.__row3Column1Button.grid_forget()
      self.__row4Column1Button.grid_forget()
      self.__row2Column2Button.grid_forget()
      self.__row3Column2Button.grid_forget()
      self.__row4Column2Button.grid_forget()
    elif len(self.__takenBoxes) <= self.EIGHT:
      self.doMove()

  def userRow3Column0ButtonEH(self): 
    userInput = 'X'
    self.__newLabel = Label(self.__window, text = 'X', font = 'Arial 50 bold')
    self.__newLabel.grid(row = self.THREE, column = 0)
    self.__startGame.addToList(userInput, self.BOX_FOUR)
    self.__row3Column0Button.grid_forget()
    self.recordBoxes(self.BOX_FOUR)
    if self.__startGame.winnerTestX():
      self.__instructions.set("You Win!")
      self.__row2Column0Button.grid_forget()
      self.__row3Column0Button.grid_forget()
      self.__row4Column0Button.grid_forget()
      self.__row2Column1Button.grid_forget()
      self.__row3Column1Button.grid_forget()
      self.__row4Column1Button.grid_forget()
      self.__row2Column2Button.grid_forget()
      self.__row3Column2Button.grid_forget()
      self.__row4Column2Button.grid_forget()
    elif len(self.__takenBoxes) <= self.EIGHT:
      self.doMove()

  def userRow4Column0ButtonEH(self):
    userInput = 'X'
    self.__newLabel = Label(self.__window, text = 'X', font = 'Arial 50 bold')
    self.__newLabel.grid(row = self.FOUR, column = 0)
    self.__startGame.addToList(userInput, self.BOX_SEVEN)
    self.__row4Column0Button.grid_forget()
    self.recordBoxes(self.BOX_SEVEN)
    if self.__startGame.winnerTestX():
      self.__instructions.set("You Win!")
      self.__row2Column0Button.grid_forget()
      self.__row3Column0Button.grid_forget()
      self.__row4Column0Button.grid_forget()
      self.__row2Column1Button.grid_forget()
      self.__row3Column1Button.grid_forget()
      self.__row4Column1Button.grid_forget()
      self.__row2Column2Button.grid_forget()
      self.__row3Column2Button.grid_forget()
      self.__row4Column2Button.grid_forget()
    elif len(self.__takenBoxes) <= self.EIGHT:
      self.doMove()

  def userRow2Column1ButtonEH(self):
    userInput = 'X'
    self.__newLabel = Label(self.__window, text = 'X', font = 'Arial 50 bold')
    self.__newLabel.grid(row = self.TWO, column = 1)
    self.__startGame.addToList(userInput, self.BOX_TWO)
    self.__row2Column1Button.grid_forget()
    self.recordBoxes(self.BOX_TWO)
    if self.__startGame.winnerTestX():
      self.__instructions.set("You Win!")
      self.__row2Column0Button.grid_forget()
      self.__row3Column0Button.grid_forget()
      self.__row4Column0Button.grid_forget()
      self.__row2Column1Button.grid_forget()
      self.__row3Column1Button.grid_forget()
      self.__row4Column1Button.grid_forget()
      self.__row2Column2Button.grid_forget()
      self.__row3Column2Button.grid_forget()
      self.__row4Column2Button.grid_forget()
    elif len(self.__takenBoxes) <= self.EIGHT:
      self.doMove()

  def userRow3Column1ButtonEH(self):
    userInput = 'X'
    self.__newLabel = Label(self.__window, text = 'X', font = 'Arial 50 bold')
    self.__newLabel.grid(row = self.THREE, column = 1)
    self.__startGame.addToList(userInput, self.BOX_FIVE)
    self.__row3Column1Button.grid_forget()
    self.recordBoxes(self.BOX_FIVE)
    if self.__startGame.winnerTestX():
      self.__instructions.set("You Win!")
      self.__row2Column0Button.grid_forget()
      self.__row3Column0Button.grid_forget()
      self.__row4Column0Button.grid_forget()
      self.__row2Column1Button.grid_forget()
      self.__row3Column1Button.grid_forget()
      self.__row4Column1Button.grid_forget()
      self.__row2Column2Button.grid_forget()
      self.__row3Column2Button.grid_forget()
      self.__row4Column2Button.grid_forget()
    elif len(self.__takenBoxes) <= self.EIGHT:
      self.doMove()

  def userRow4Column1ButtonEH(self):
    userInput = 'X'
    self.__newLabel = Label(self.__window, text = 'X', font = 'Arial 50 bold')
    self.__newLabel.grid(row = self.FOUR, column = 1)
    self.__startGame.addToList(userInput, self.BOX_EIGHT)
    self.__row4Column1Button.grid_forget()
    self.recordBoxes(self.BOX_EIGHT)
    if self.__startGame.winnerTestX():
      self.__instructions.set("You Win!")
      self.__row2Column0Button.grid_forget()
      self.__row3Column0Button.grid_forget()
      self.__row4Column0Button.grid_forget()
      self.__row2Column1Button.grid_forget()
      self.__row3Column1Button.grid_forget()
      self.__row4Column1Button.grid_forget()
      self.__row2Column2Button.grid_forget()
      self.__row3Column2Button.grid_forget()
      self.__row4Column2Button.grid_forget()
    elif len(self.__takenBoxes) <= self.EIGHT:
      self.doMove()

  def userRow2Column2ButtonEH(self):
    userInput = 'X'
    self.__newLabel = Label(self.__window, text = 'X', font = 'Arial 50 bold')
    self.__newLabel.grid(row = self.TWO, column = self.TWO)
    self.__startGame.addToList(userInput, self.BOX_THREE)
    self.__row2Column2Button.grid_forget()
    self.recordBoxes(self.BOX_THREE)
    if self.__startGame.winnerTestX():
      self.__instructions.set("You Win!")
      self.__row2Column0Button.grid_forget()
      self.__row3Column0Button.grid_forget()
      self.__row4Column0Button.grid_forget()
      self.__row2Column1Button.grid_forget()
      self.__row3Column1Button.grid_forget()
      self.__row4Column1Button.grid_forget()
      self.__row2Column2Button.grid_forget()
      self.__row3Column2Button.grid_forget()
      self.__row4Column2Button.grid_forget()
    elif len(self.__takenBoxes) <= self.EIGHT:
      self.doMove()

  def userRow3Column2ButtonEH(self):
    userInput = 'X'
    self.__newLabel = Label(self.__window, text = 'X', font = 'Arial 50 bold')
    self.__newLabel.grid(row = self.THREE, column = self.TWO)
    self.__startGame.addToList(userInput, self.BOX_SIX)
    self.__row3Column2Button.grid_forget()
    self.recordBoxes(self.BOX_SIX)
    if self.__startGame.winnerTestX():
      self.__instructions.set("You Win!")
      self.__row2Column0Button.grid_forget()
      self.__row3Column0Button.grid_forget()
      self.__row4Column0Button.grid_forget()
      self.__row2Column1Button.grid_forget()
      self.__row3Column1Button.grid_forget()
      self.__row4Column1Button.grid_forget()
      self.__row2Column2Button.grid_forget()
      self.__row3Column2Button.grid_forget()
      self.__row4Column2Button.grid_forget()
    elif len(self.__takenBoxes) <= self.EIGHT:
      self.doMove()

  def userRow4Column2ButtonEH(self):
    userInput = 'X'
    self.__newLabel = Label(self.__window, text = 'X', font = 'Arial 50 bold')
    self.__newLabel.grid(row = self.FOUR, column = self.TWO)
    self.__startGame.addToList(userInput, self.BOX_NINE)
    self.__row4Column2Button.grid_forget()
    self.recordBoxes(self.BOX_NINE)
    if self.__startGame.winnerTestX():
      self.__instructions.set("You Win!")
      self.__row2Column0Button.grid_forget()
      self.__row3Column0Button.grid_forget()
      self.__row4Column0Button.grid_forget()
      self.__row2Column1Button.grid_forget()
      self.__row3Column1Button.grid_forget()
      self.__row4Column1Button.grid_forget()
      self.__row2Column2Button.grid_forget()
      self.__row3Column2Button.grid_forget()
      self.__row4Column2Button.grid_forget()
    elif len(self.__takenBoxes) <= self.EIGHT:
      self.doMove()       

#Lots of unsuccessful attempts to get input for game mode
#Kept for reference of debugging purposes



#Vincent Preikstas ----------------------------------------------
'''
def main():
  gameMode = input("Imput 1 for test Mode, Enter for Regular Mode")
  gameGUI(gameMode)
'''
##theMode = input('Please god Work: ')
##print(theMode)
##main(
##gameGUI()
'''
gameMode = input("Imput 1 for test Mode, Enter for Regular Mode")
print(gameMode)
if gameMode == "1":
  gameGUI(1)
else:
  gameGUI()
gameGUI(gameMode)
'''




gameGUI()
