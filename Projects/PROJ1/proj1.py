# File:        proj1.py
# Author:      Robert Rose
# Date:        11/10/15
# Section:     11
# E-mail:      robrose2@umbc.edu
# Description: This program is an implementation of Conway's game of life.
#              It takes relevant data from the user to construct a game
#              board and allows a user to cycle through the game.


# Main function to run code.
def main():

    #: Number of rows on the board.
    rows = int(input("Please input the number of rows (min. 1): "))
    while rows < 1:
        rows = int(input("Invalid input. Please input the number of rows (min. 1): "))

    #: Number of columns on the board.
    cols = int(input("Please input the number of columns (min. 1): "))
    while cols < 1:
        cols = int(input("Invalid input. Please input the number of columns (min. 1): "))
    
    board = constructBoard(cols, rows)
    printBoard(board)

# Prints the contents of the board out using for loops.
def printBoard(board):
    for row in board:
        rowStr = ""
        for col in row:
            rowStr += col
        print(rowStr)

# Generates a board and fills it with periods
def constructBoard(width, height):
    board = [['.' for x in range(width)] for y in range(height)]
    return board

def nextIteration():
    return


main()