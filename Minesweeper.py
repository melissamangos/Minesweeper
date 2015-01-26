# Melissa Mangos
# May, 13th 2013
# This program plays a game of minesweeper.

# Import random
import random

# FUNCTIONS ----------------------------------------------------------------------------------------

# Sets up the game board from amount of rows and columns inputted
def setUpBoard (numRows, numCols):
    gameBoard = [[[0, 0] for i in range (numCols)] for j in range (numRows)]
    return gameBoard

# assigns Bombs to squares
def assignBombs (numRows, numCols, gameBoard):
    # Gets random Rows and Columns
    bombRow = random.randint (0, numRows - 1)
    bombCol = random.randint (0, numCols - 1)
    if (gameBoard[bombRow][bombCol][1] == -1):
        assignBombs (numRows, numCols, gameBoard)
    else:
        gameBoard[bombRow][bombCol][1] = -1      
    return None

# Counts number of bombs around squares
def countBombs (gameBoard, numRows, numCols):   
    for row in range (0, numRows):
        for col in range (0, numCols):
            if (gameBoard[row][col][1] != -1):
                # Counts bombs from the top left
                if (col - 1 >= 0) and (row - 1 >= 0) and (gameBoard[row - 1][col - 1][1] == -1):
                    gameBoard[row][col][1] += 1
                # Top middle
                if (row - 1 >= 0) and (gameBoard[row - 1][col][1] == -1):
                    gameBoard[row][col][1] += 1
                # Top right
                if (col + 1 < numCols) and (row - 1 >= 0) and (gameBoard[row - 1][col + 1][1] == -1):
                    gameBoard[row][col][1] += 1
                # Left
                if (col - 1 >= 0) and (gameBoard[row][col - 1][1] == -1):
                    gameBoard[row][col][1] += 1
                # Right
                if (col + 1 < numCols) and (gameBoard[row][col + 1][1] == -1):
                    gameBoard[row][col][1] += 1
                # Bottom left
                if (col - 1 >= 0) and (row + 1 < numRows) and (gameBoard[row + 1][col - 1][1] == -1):
                    gameBoard[row][col][1] += 1
                # Bottom middle
                if (row + 1 < numRows) and (gameBoard[row + 1][col][1] == -1): 
                    gameBoard[row][col][1] += 1
                # Bottom right
                if (col + 1 < numCols) and (row + 1 < numRows) and (gameBoard[row + 1][col + 1][1] == -1):
                    gameBoard[row][col][1] += 1
    return None

# uncovers a specific square
def uncoverSquares (row, col, gameBoard, numRows, numCols):
    # Globalizes variable
    global uncovered
    
    # uncovers top left
    if (col - 1 >= 0) and (row - 1 >= 0) and (gameBoard[row - 1][col - 1][0] == 0):
        gameBoard[row - 1][col - 1][0] = 1
        uncovered = uncovered + 1
        if (gameBoard[row - 1][col - 1][1] == 0):
            # If the square has no mines, calls functions for new square
            uncoverSquares (row - 1, col - 1, gameBoard, numRows, numCols)
    # Top middle
    if (row - 1 >= 0) and (gameBoard[row - 1][col][0] == 0):
        gameBoard[row - 1][col][0] = 1
        uncovered = uncovered + 1
        if (gameBoard[row - 1][col][1] == 0):
            # If the square has no mines, calls functions for new square
            uncoverSquares (row - 1, col, gameBoard, numRows, numCols)
    # Top right
    if (col + 1 < numCols) and (row - 1 >= 0) and (gameBoard[row - 1][col + 1][0] == 0):
        gameBoard[row - 1][col + 1][0] = 1
        uncovered = uncovered + 1
        if (gameBoard[row - 1][col + 1][1] == 0):
            # If the square has no mines, calls functions for new square
            uncoverSquares (row - 1, col + 1, gameBoard, numRows, numCols)
    # Left
    if (col - 1 >= 0) and (gameBoard[row][col - 1][0] == 0):
        gameBoard[row][col - 1][0] = 1
        uncovered = uncovered + 1
        if (gameBoard[row][col - 1][1] == 0):
            # If the square has no mines, calls functions for new square
            uncoverSquares (row, col - 1, gameBoard, numRows, numCols)
    # Right
    if (col + 1 < numCols) and (gameBoard[row][col + 1][0] == 0):
        gameBoard[row][col + 1][0] = 1
        uncovered = uncovered + 1
        if (gameBoard[row][col + 1][1] == 0):
            # If the square has no mines, calls functions for new square
            uncoverSquares (row, col + 1, gameBoard, numRows, numCols)
    # Bottom left
    if (col - 1 >= 0) and (row + 1 < numRows) and (gameBoard[row + 1][col - 1][0] == 0):
        gameBoard[row + 1][col - 1][0] = 1
        uncovered = uncovered + 1
        if (gameBoard[row + 1][col - 1][1] == 0):
            # If the square has no mines, calls functions for new square
            uncoverSquares (row + 1, col - 1, gameBoard, numRows, numCols)
    # Bottom middle
    if (row + 1 < numRows) and (gameBoard[row + 1][col][0] == 0):
        gameBoard[row + 1][col][0] = 1
        uncovered = uncovered + 1
        if (gameBoard[row + 1][col][1] == 0):
            # If the square has no mines, calls functions for new square
            uncoverSquares (row + 1, col, gameBoard, numRows, numCols)
    # Bottom right
    if (col + 1 < numCols) and (row + 1 < numRows) and (gameBoard[row + 1][col + 1][0] == 0):
        gameBoard[row + 1][col + 1][0] = 1
        uncovered = uncovered + 1
        if (gameBoard[row + 1][col + 1][1] == 0):
            # If the square has no mines, calls functions for new square
            uncoverSquares (row + 1, col + 1, gameBoard, numRows, numCols)
    
    return None

# Inputs a row and column
def inputPos (gameBoard, numRows, numCols):
    # Globalizes variables
    global uncovered
    global gameOver
    global flagged
    
    # Input
    square = int (input ('Would you like to 1 (select a square) or 2 (flag a square as a mine)? '))
    row = int (input ('Enter a row: '))
    col = int (input ('Enter a column: '))

    # Adjust varibles to match numbers in array
    row = row - 1
    col = col - 1

    # Select a square
    if (square == 1):
        # The square has no mines around it
        if (gameBoard[row][col][1] == 0):
            gameBoard[row][col][0] = 1
            uncovered = uncovered + 1
            # uncovers squares around it
            uncoverSquares (row, col, gameBoard, numRows, numCols)
        # The square is a mine
        elif (gameBoard[row][col][1] == -1):
            print ('You hit a mine!')
            gameOver = 'true'
            print ('You Lost!')
        # The square is a number
        else:
            gameBoard[row][col][0] = 1
            uncovered = uncovered + 1
    # Flag a square
    elif (square == 2):
        # The square is a mine
        if (gameBoard[row][col][1] == -1):
            gameBoard[row][col][0] = 2
        # The square is not a mine
        else:
            # If the player flags three non-mines the game is over
            flagged = flagged - 1
            gameBoard[row][col][0] = 2
    return None

# Display game board
def displayBoard (gameBoard, numRows, numCols):
    # Globalize variables
    global gameOver

    # Initialize display list
    dispRow = []
    
    for row in range (0, numRows):
        for col in range (0, numCols):
            # Covered
            if (gameOver == 'false') and (gameBoard[row][col][0] == 0):
                dispRow.append ('X')
            # flagged
            elif (gameOver == 'false') and (gameBoard[row][col][0] == 2):
                dispRow.append ('F')
            # Mine (if the game is over)
            elif (gameOver == 'true') and (gameBoard[row][col][1] == -1):
                dispRow.append ('M')
            # number
            else:
                dispRow.append (str (gameBoard[row][col][1]))
        # Displays one row of data
        print (dispRow)

        # Resets list
        dispRow = []
    return None

# MAIN PROGRAM -------------------------------------------------------------------------------------

# Initialize variables
gameOver = 'false'
flagged = 3

# Input values
numRow = int (input ('Enter the number of rows: '))
numCol = int (input ('Enter the number of columns: '))
numBombs = int (input ('Enter the number of bombs: '))

# Find out the number of covered spaces
uncovered = 0
covered = (numRow * numCol) - numBombs

# Sets up board according to inputted values
board = setUpBoard (numRow, numCol)

# Randomly assigns bombs to squares
for k in range (0, numBombs):
    assignBombs (numRow, numCol, board)

# Counts the number of bombs around all squares
countBombs (board, numRow, numCol)
        
# Displays the board
displayBoard (board, numRow, numCol)

# Plays the game
while (gameOver == 'false'):
    # Inputs a square and uncovers squares
    inputPos (board, numRow, numCol)

    # Checks if the game is over
    # If all squares except mines are uncovered
    if (uncovered == covered):
        gameOver = 'true'
        print ('')
        print ('You won!')
    # If non-mines are flagged
    if (flagged == 0):
        gameOver = 'true'
        print ('')
        print ('You Lost!')
        
    # Displays the board
    displayBoard (board, numRow, numCol)
        

