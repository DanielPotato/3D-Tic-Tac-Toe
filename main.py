board = ["", "-", "",
         "-", "-", "-",
         "-", "-", "-"]
current_player = "X"
winner = None
gamerunning = True


def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board[3] + '|' + board[4] + '|' + board[5])
    print("------")
    print(board[6] + '|' + board[7] + '|' + board[8])


def playerInput(board):
    inp = int(input("Enter a number from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = current_player
    else:
        print("Oops, player is already in that spot.")


def checkhoriziontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkrow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def checktie(board):
    global gamerunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        gamerunning = False


def checkforwin(board):
    if checkDiag(board) or checkrow(board) or checkhoriziontal(board):
        gamerunning = False
        printBoard(board)
        print(f"The winner is {winner}")


def switchplayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


while gamerunning:
    printBoard(board)
    playerInput(board)
    checkforwin(board)
    checktie(board)
    switchplayer()
    if gamerunning == False:
        break
