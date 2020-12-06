#Tic-Tac-Toe
import random

board = {1:' ',2:' ',3:' ',
         4:' ',5:' ',6:' ',
         7:' ',8:' ',9:' '}
boardHelp = {1:'1',2:'2',3:'3',
         4:'4',5:'5',6:'6',
         7:'7',8:'8',9:'9'}
player = ''
whoseMove = 'X'
moveNumber = 9

def printBoard(board):
    print(board[1]+"|"+board[2]+"|"+board[3])
    print('-----')
    print(board[4]+"|"+board[5]+"|"+board[6])
    print('-----')
    print(board[7]+"|"+board[8]+"|"+board[9]+'\n')

def resetGame():
    global board
    global player
    global whoseMove
    global moveNumber
    global win
    
    board = board = {1:' ',2:' ',3:' ',
         4:' ',5:' ',6:' ',
         7:' ',8:' ',9:' '}
    player = ''
    whoseMove = 'X'
    moveNumber = 9

def selectPlayer():
    print('Do you want to be X or O?')
    playerInput = input()

    if playerInput.upper() == 'X':
        print('You will go first!')
    elif playerInput.upper() == 'O':
        print('The computer will go first!')
    else:
        print('Please choose either X or O.')
        selectPlayer()

    return playerInput.upper()

def changeWhoseMove():
    global whoseMove
    global moveNumber
    if whoseMove == 'X':
        whoseMove = 'O'
    elif whoseMove == 'O':
        whoseMove = 'X'
    moveNumber -= 1
    
def computerMove():
    openSpace = False
    intLocation = random.randint(1,9)
    
    #Don't let a move overwrite an existing placement
    while openSpace == False:
        if board[intLocation] != ' ':
            intLocation = random.randint(1,9)
        else:
            board[intLocation] = whoseMove
            openSpace = True
    
    print('The computer moved to space ' + str(intLocation))
    changeWhoseMove()
    printBoard(board)
    

def userMove():
    print('''Where would you like to move? Type 'help' for help.''')
    move = input()

    if move.lower() == 'help':
        printBoard(boardHelp)
    elif int(move)<1 or int(move)>9:
        print('Please type a value between 1-9')
        changeWhoseMove()
    elif board[int(move)] != ' ':
        print('Invalid move! That space is already taken')
        userMove()
    else:
        board[int(move)] = whoseMove
        if not checkWin():
            changeWhoseMove()
    printBoard(board)

def checkWin():
    global win
    
    for r in range(1,8,3):
        #Check rows
        if board[r] == board[r+1] == board[r+2] == whoseMove:
            print(str(whoseMove) + ' is the winner!')
            return True
        #Check columns
        for c in range(1,4):
            if board[c] == board[c+3] == board[c+6] == whoseMove:
                print(str(whoseMove) + ' is the winner!')
                return True
    #Check diagonal
    if board[1] == board[5] == board[9] == whoseMove:
        print(str(whoseMove) + ' is the winner!')
        return True
    elif board[3] == board[5] == board[7] == whoseMove:
        print(str(whoseMove) + ' is the winner!')
        return True
    return False

def main():
    global player
    win = False
    
    player = selectPlayer()
    while (moveNumber > 0) and (win == False):
        win = checkWin()
        if win == True:
            break
        else:
            if whoseMove == player:
                userMove()
            else:
                computerMove()
    if moveNumber == 0:
        checkWin()
    print('''Play again? (Y/N)''')
    playAgain = input().upper()
    if playAgain == 'Y':
        resetGame()
        main()
    else:
        quit

#Execute    
main()        

