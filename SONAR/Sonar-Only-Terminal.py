import random
import sys
import math


def getNewBoard():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def drawBoard(board):
    tensDigitsLine = '    '
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)


    for row in range(15):
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

        print(f'{extraSpace}{row} {boardRow} {row}')

    print()
    print(tensDigitsLine)
    print('   ' + ('0123456789' * 6))

def getRandomChests(numChests):
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
        if newChest not in chests:
            chests.append(newChest)
    return chests

def isOnBoard(x, y):
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    smallestDistance = 100
    for chest in chests:
        distance = math.sqrt((chest[0] - x) ** 2 + (chest[1] - y) ** 2)

        if distance < smallestDistance:
            smallestDistance = distance

    smallestDistance = round(smallestDistance)

    if smallestDistance == 0:
        chests.remove([x, y])
        return 'You found a sunken treasure chest!'
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return f'Treasure detected at a distance of {smallestDistance} from the sonar device.'
        else:
            board[x][y] = 'X'
            return 'Sonar did not detect anything. All treasure chests out of range.'
def enterPlayerMove():
    print('Where do you want to drop the next sonar device? (0-59 0-14)')
    while True:
        move = input()
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit():
            x = int(move[0])
            y = int(move[1])
            if isOnBoard(x, y):
                return [x, y]
        print('Enter a valid move. (0-59 0-14)')

def showInstructions():
    print('''Instructions:
You are the captain of the SS Explorer, a ship exploring the deep ocean. Your goal is to find all the sunken treasure chests before your sonar devices run out of power.
enter the coordinates to drop a sonar device. The sonar device will give you a number indicating how many units away the nearest treasure chest is. For example, if the sonar device returns a 3, that means there is a treasure chest 3 units away from the device in any direction (including diagonals). If it returns a 0, that means you found a treasure chest! If it returns an X, that means there are no treasure chests within range of the sonar device.
You have 20 sonar devices. Good luck! press enter to continue...''')
    input()

    print('''When you drop a sonar device, it will give you a number indicating how many units away the nearest treasure chest is. For example, if the sonar device returns a 3, that means there is a treasure chest 3 units away from the device in any direction (including diagonals). If it returns a 0, that means you found a treasure chest! If it returns an X, that means there are no treasure chests within range of the sonar device.
You have 20 sonar devices. Good luck! press enter to begin...''')
    input()

print('S O N A R !')
showInstructions()
print("Would you like to view the instructions again? (yes/no)")
if input().lower().startswith('y'):
    showInstructions()

while True:
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)

    while sonarDevices > 0:
        print(f'You have {sonarDevices} sonar device(s) left. There are {len(theChests)} treasure chest(s) remaining.')
        x, y = enterPlayerMove()
        result = makeMove(theBoard, theChests, x, y)
        print(result)
        drawBoard(theBoard)

        if len(theChests) == 0:
            print('Congratulations! You found all the sunken treasure chests!')
            break

        sonarDevices -= 1

    if sonarDevices == 0:
        print('Game over! You ran out of sonar devices!')
        print('The remaining chests were here:')
        for chest in theChests:
            print(f' {chest[0]} {chest[1]}')

    print('Do you want to play again? (yes/no)')
    if not input().lower().startswith('y'):
        sys.exit() 