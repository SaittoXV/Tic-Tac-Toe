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
        if len(hasDigit) == 0:
            break
        else:
            user_input = int(input("enter your move number: "))
            userTurn(board,user_input)
            computerTurn(board)
            drawBorder(board)

def computerTurn(board):
    hasFound = False
    computer_choose = randrange(1,10)
    print(computer_choose)
    for indexRow,row in enumerate(board):
        for indexCol,col in enumerate(row):
            if col == "X" or col == "O":
                continue
            elif computer_choose == col:
                board[indexRow][indexCol] = "X"
                hasFound = True
                break
            elif hasFound == False and indexRow == len(board)-1 and indexCol == len(row)-1:
                print("recurse")
                return computerTurn(board)
        if hasFound:
            return board
            break

def userTurn(board,user_input):
    for indexRow,row in enumerate(board):
        for indexCol,col in enumerate(row):
            if user_input == col:
                board[indexRow][indexCol] = "O"
                return board

if __name__ == "__main__":
    main()
    