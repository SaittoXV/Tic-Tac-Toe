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
    print(board)
    
   #user_input = int(input("enter your move number: "))


def computerTurn(board):
    computer_choose = randrange(1,10)
    for indexRow,row in enumerate(board):
        for indexCol,col in enumerate(row):
            if computer_choose == col:
                board[indexRow][indexCol] = "X"

if __name__ == "__main__":
    main()
    