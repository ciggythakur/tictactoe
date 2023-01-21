board =[ "-","-","-",
        "-","-","-",
        "-","-","-"]

currentPlayer ="X"
winner = None 
gameRunning = True


#printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
   


#player input
def playerInput(board):
    inp = int(input("Enter a number 1-9"))
    if inp>= 1 and inp <=9 and board [inp-1]== "-":
        board[inp-1]= currentPlayer
    else:
        print("Oops player occupied the position")


#check for win or tie
def checkHorizontal(board):
    global gameRunning
    if board[0]==board[1]==board[2]!="-":
        winner = board[0]
        return False
    elif board[3]==board[4]==board[5]!="-":
        winner = board[3]
        return False
    elif board[6]==board[7]==board[8]!="-":
        winner = board[6]
        return False

def checkVertical(board):
    global gameRunning
    if board[0]==board[3]==board[6]!="-":
        winner = board[0]
        return False 

    elif board[1]==board[4]==board[7]!="-":
        winner = board[1]
        return False
    elif board[2]==board[5]==board[8]!="-":
        winner = board[2]
        return False

def checkDiagonal(board):
    global gameRunning
    if board[0]==board[4]==board[8]!="-":
        winner = board[0]
        return False
    elif board[2]==board[4]==board[6]!="-":
        winner = board[2]
        return False

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Its a Tie")
        gameRunning = False    

def checkWin(board):
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        print(f"The winner is {winner}")

# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer ="X"

# check for win or tie
while gameRunning:
    printBoard(board)
    playerInput(board)
    
    checkWin(board)
    checkTie(board)
    switchPlayer()
