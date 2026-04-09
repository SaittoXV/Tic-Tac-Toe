from random import randrange

def drawBorder(board):
    print("+-------"*3,"+",sep="")
    for row in range(3):
        print("|       "*3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end = "")
        print("|")
        print("|       "*3,"|", sep="")
        print("+-------"*3,"+",sep="")

def main():
    board = [[1,2,3],[4,5,6],[7,8,9]]
    computerTurn(board)
    drawBorder(board)

    while True:
        hasDigit = [True for row in board for col in row if type(col) == int]
        hasWon,userWon = checkWinner(board)
        if hasWon:
            drawBorder(board)
            if userWon:
                print("You Won!!")
            else:
                print("Computer Won!!")
            break
        elif len(hasDigit) == 0:
            break
        user_input = int(input("enter your move number: "))
        userTurn(board,user_input)
        computerTurn(board)
        drawBorder(board)

def computerTurn(board):
    computer_choose = randrange(1,10)
    print(computer_choose)
    for indexRow,row in enumerate(board):
        for indexCol,col in enumerate(row):
            if computer_choose == col:
                board[indexRow][indexCol] = "X"
                return board
            elif indexRow == len(board)-1 and indexCol == len(row)-1:
                print("recurse")
                return computerTurn(board)

def userTurn(board,user_input):
    for indexRow,row in enumerate(board):
        for indexCol,col in enumerate(row):
            if user_input == col:
                board[indexRow][indexCol] = "O"
                return board
            
def checkWinner(board):
    for index in range(3):
        if board[index][0] == board[index][1] and board[index][0] == board[index][2]:
            if board[index][0] == "O":
                return True,True
            return True,False
        elif board[0][index] == board[1][index] and board[0][index] == board[2][index]:
            if board[0][index] == "O":
                return True,True
            return True,False
        elif board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            if board[0][0] == "O":
                return True,True
            return True,False
        elif board[0][2] == board[1][1] and board[0][0] == board[2][0]:
            if board[0][2] == "O":
                return True,True
            return True,False
    return False,False

if __name__ == "__main__":
    main()