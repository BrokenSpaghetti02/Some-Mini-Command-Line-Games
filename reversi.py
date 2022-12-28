def main():
    N = int(input("Enter board size: "))
    gameBoard = [[0 for i in range(N)] for j in range(N)]
    initGameBoard(gameBoard, N)    
    numberOfBlocks = int(input("Enter number of blocks: "))
    
    while numberOfBlocks > (N ** 2) / 2:
        print("Too many blocks!")
        numberOfBlocks = int(input("Enter number of blocks: "))
    
    # Gets the number of blocks and inputs the blocks on the board

    for i in range(numberOfBlocks):
        block = input("Enter position for block {}: ".format(i + 1)).upper()
        blockX = convertPos(block)[0]
        blockY = convertPos(block)[1]
        while blockX >= N or blockY >= N:
            print("Invalid Position!")
            block = input("Enter position for block {}: ".format(i + 1)).upper()
            blockX = convertPos(block)[0]
            blockY = convertPos(block)[1]
            if gameBoard[blockY][blockX] != "." or gameBoard[blockY][blockX] == "#":
                print("Invalid Position!")
                block = input("Enter position for block {}: ".format(i + 1)).upper()
                blockX = convertPos(block)[0]
                blockY = convertPos(block)[1]
            else:
                continue
        
        while gameBoard[blockY][blockX] != "." or gameBoard[blockY][blockX] == "#":
            print("Invalid Position!")
            block = input("Enter position for block {}: ".format(i + 1)).upper()
            blockX = convertPos(block)[0]
            blockY = convertPos(block)[1]
            if blockX >= N or blockY >= N:
                print("Invalid Position!")
                block = input("Enter position for block {}: ".format(i + 1)).upper()
                blockX = convertPos(block)[0]
                blockY = convertPos(block)[1]
            else:
                continue

        addBlock(gameBoard, blockY, blockX)

    # Main game loop starts here    

    round = 1
    gamePassed = 0
    while True:
        p = "X"
        print("Round {}: ".format(round))
        printGameBoard(gameBoard, N)
        if has_valid_moves(gameBoard, p):
            pos = input("Player {}'s turn: ".format(p)).upper()
            x = convertPos(pos)[0]
            y = convertPos(pos)[1]

            while not valid_move(gameBoard, p , y, x, flip = False):
                print("Invalid Position!")
                pos = input("Player {}'s turn: ".format(p)).upper()
                x = convertPos(pos)[0]
                y = convertPos(pos)[1]
            
            if valid_move(gameBoard, p, y, x, flip = False):
                valid_move(gameBoard, p, y, x, flip = True)
            round += 1
        
        else:
            print("Player {} has no valid moves! Pass!".format(p))
            gamePassed += 1
            round += 1
            if gamePassed == 2:
                break

        p = "O"
        print("Round {}: ".format(round))
        printGameBoard(gameBoard, N)
        if has_valid_moves(gameBoard, p):
            pos = input("Player {}'s turn: ".format(p)).upper()
            x = convertPos(pos)[0]
            y = convertPos(pos)[1]

            while not valid_move(gameBoard, p , y, x, flip = False):
                print("Invalid Position!")
                pos = input("Player {}'s turn: ".format(p)).upper()
                x = convertPos(pos)[0]
                y = convertPos(pos)[1]
            
            if valid_move(gameBoard, p, y, x, flip = False):
                valid_move(gameBoard, p, y, x, flip = True)
            round += 1
        
        else:
            print("Player {} has no valid moves! Pass!".format(p))
            gamePassed += 1
            round += 1
            if gamePassed == 2:
                break


    numX = 0
    numO = 0
    if not has_empty_cells(gameBoard):
        for i in range(N):
            for j in range(N):
                if gameBoard[i][j] == "X":
                    numX += 1
                elif gameBoard[i][j] == "O":
                    numO += 1
    
    if numX > numO:
        print("Game over: ")
        printGameBoard(gameBoard, N)
        print("Player X wins!")
    elif numX == numO:
        print("Game over: ")
        printGameBoard(gameBoard, N)
        print("Draw Game!")
    else:
        print("Game over: ")
        printGameBoard(gameBoard, N)
        print("Player O wins!")

# Initializes gameboard

def initGameBoard(gameBoard, N):
    half = int(N/2) - 1
    for i in range(N):   
        for j in range(N):
            if i == half and j == half:
                gameBoard[i][j] = "X"
            elif i == half and j == half + 1:
                gameBoard[i][j] = "O"
            elif i == half + 1 and j == half:
                gameBoard[i][j] = "O"
            elif i == half + 1 and j == half + 1:
                gameBoard[i][j] = "X"
            else:
                gameBoard[i][j] = "."

# Prints the gameboard

def printGameBoard(gameBoard, N):
    if N < 10:
        print(" ", end = "")
    else:
        print("  ", end = "")
    for i in range(N):
        if i == N - 1:
            print(" {}".format(chr(65 + i)))
        else:
            print(" {}".format(chr(65 + i)), end = "")
    for row in range(N):
        if N < 10:
            print("{} ".format(row + 1), end = "")
        else:
            if row < 9:
                print(" {} ".format(row + 1), end = "")
            else:
                print("{} ".format(row + 1), end = "")
        for column in range(N):
            if column == N - 1:
                print("{}".format(gameBoard[row][column]))
            else:
                print("{} ".format(gameBoard[row][column]), end = "")

# Converts the user inputs of positions into an array

def convertPos(userInput):
    pos_arr = []
    pos_arr.append(ord(userInput[0]) - 65)
    pos_arr.append(int(userInput[1:]) - 1)

    return pos_arr

# Adds blocks on the gameboard

def addBlock(gameBoard, blockY, blockX):
    gameBoard[blockY][blockX] = "#"

# This took me 8 hours to figure out and fix all the bugs
# If there are still bugs then either I am dumb or I was on drugs
# Please at least let me know through email if there were bugs cuz I wanna know where I f'ed up
# Sorru for bad langage

def valid_move(gameBoard, p, y, x, flip = False):

    # Check if valid move, return true
    # Had to check all 8 directions up, down, right, left, upright, upleft, downright, downleft
    # Then had to do it more 8 times for implementing the flip :(

    if flip == False:
        count = 0
        if x - 1 >= 0 and gameBoard[y][x - 1] != "." and gameBoard[y][x - 1] != p and gameBoard[y][x - 1] != "#":
            while x - 2 - count >= 0:
                if gameBoard[y][x - 2 - count] == p:
                    return True
                else:
                    if gameBoard[y][x - 2 - count] == "." or gameBoard[y][x - 2 - count] == "#":
                        break
                    else:
                        count += 1
        count = 0
        if x + 1 <= len(gameBoard) - 1 and gameBoard[y][x + 1] != "." and gameBoard[y][x + 1] != p and gameBoard[y][x + 1] != "#":
            while x + 2 + count <= len(gameBoard) - 1:
                if gameBoard[y][x + 2 + count] == p:
                    return True
                else:
                    if gameBoard[y][x + 2 + count] == "." or gameBoard[y][x + 2 + count] == "#":
                        break
                    else:
                        count += 1
        count = 0
        if y - 1 >= 0 and gameBoard[y - 1][x] != "." and gameBoard[y - 1][x] != p and gameBoard[y - 1][x] != "#":
            while y - 2 - count >= 0:
                if gameBoard[y - 2 - count][x] == p:
                    return True
                else:
                    if gameBoard[y - 2 - count][x] == "." or gameBoard[y - 2 - count][x] == "#":
                        break
                    else:
                        count += 1
        count = 0
        if y + 1 <= len(gameBoard) - 1 and gameBoard[y + 1][x] != "." and gameBoard[y + 1][x] != p and gameBoard[y + 1][x] != "#":
            while y + 2 + count <= len(gameBoard) - 1:
                if gameBoard[y + 2 + count][x] == p:
                    return True
                else:
                    if gameBoard[y + 2 + count][x] == "." or gameBoard[y + 2 + count][x] == "#":
                        break
                    else:
                        count += 1
        count = 0
        if x - 1 >= 0 and y - 1 >= 0 and gameBoard[y - 1][x - 1] != "." and gameBoard[y - 1][x - 1] != p and gameBoard[y - 1][x - 1] != "#":
            while (y - 2 - count >= 0) and (x - 2 - count >= 0):
                if gameBoard[y - 2 - count][x - 2 - count] == p:
                    return True
                else:
                    if gameBoard[y - 2 - count][x - 2 - count] == "." or gameBoard[y - 2 - count][x - 2 - count] == "#":
                        break
                    else:
                        count += 1
        count = 0
        if x + 1 <= len(gameBoard) - 1 and y - 1 >= 0 and gameBoard[y - 1][x + 1] != "." and gameBoard[y - 1][x + 1] != p and gameBoard[y - 1][x + 1] != "#":
            while (y - 2 - count >= 0) and (x + 2 + count <= len(gameBoard) - 1):
                if gameBoard[y - 2 - count][x + 2 + count] == p:
                    return True
                else:
                    if gameBoard[y - 2 - count][x + 2 + count] == "." or gameBoard[y - 2 - count][x + 2 + count] == "#":
                        break
                    else:
                        count += 1
        count = 0
        if x - 1 >= 0 and y + 1 <= len(gameBoard) - 1 and gameBoard[y + 1][x - 1] != "." and gameBoard[y + 1][x - 1] != p and gameBoard[y + 1][x - 1] != "#":
            while (y + 2 + count <= len(gameBoard) - 1) and (x - 2 - count >= 0):
                if gameBoard[y + 2 + count][x - 2 - count] == p:
                    return True
                else:
                    if gameBoard[y + 2 + count][x - 2 - count] == "." or gameBoard[y + 2 + count][x - 2 - count] == "#":
                        break
                    else:
                        count += 1
        count = 0
        if x + 1 <= len(gameBoard) - 1 and y + 1 <= len(gameBoard) - 1 and gameBoard[y + 1][x + 1] != "." and gameBoard[y + 1][x + 1] != p and gameBoard[y + 1][x + 1] != "#":
            while (y + 2 + count <= len(gameBoard) - 1) and (x + 2 + count <= len(gameBoard) - 1):
                if gameBoard[y + 2 + count][x + 2 + count] == p:
                    return True
                else:
                    if gameBoard[y + 2 + count][x + 2 + count] == "." or gameBoard[y + 2 + count][x + 2 + count] == "#":
                        break
                    else:
                        count += 1
        count = 0

    # Perform move, return none
    # Save me :)

    else:
        count = 0
        if x - 1 >= 0 and gameBoard[y][x - 1] != "." and gameBoard[y][x - 1] != p and gameBoard[y][x - 1] != "#":
            while x - 2 - count >= 0:
                if gameBoard[y][x - 2 - count] == p:
                    count += 1
                    gameBoard[y][x] = p
                    for i in range(count):
                        gameBoard[y][x - 1 - i] = p
                    break
                else:
                    if gameBoard[y][x - 2 - count] == "." or gameBoard[y][x - 2 - count] == "#":
                        count = 0
                        break
                    else:
                        count += 1
        count = 0
        if x + 1 <= len(gameBoard) - 1 and gameBoard[y][x + 1] != "." and gameBoard[y][x + 1] != p and gameBoard[y][x + 1] != "#":
            while x + 2 + count <= len(gameBoard) - 1:
                if gameBoard[y][x + 2 + count] == p:
                    count += 1
                    for i in range(count):
                        gameBoard[y][x + 1 + i] = p
                    break
                else:
                    if gameBoard[y][x + 2 + count] == "." or gameBoard[y][x + 2 + count] == "#":
                        count = 0
                        break
                    else:
                        count += 1
        gameBoard[y][x] = p
        count = 0
        if y - 1 >= 0 and gameBoard[y - 1][x] != "." and gameBoard[y - 1][x] != p and gameBoard[y - 1][x] != "#":
            while y - 2 - count >= 0:
                if gameBoard[y - 2 - count][x] == p:
                    count += 1
                    for i in range(count):
                        gameBoard[y - 1 - i][x] = p
                    break
                else:
                    if gameBoard[y - 2 - count][x] == "." or gameBoard[y - 2 - count][x] == "#":
                        count = 0
                        break
                    else:
                        count += 1
        gameBoard[y][x] = p
        count = 0
        if y + 1 <= len(gameBoard) - 1 and gameBoard[y + 1][x] != "." and gameBoard[y + 1][x] != p and gameBoard[y + 1][x] != "#":
            while y + 2 + count <= len(gameBoard) - 1:
                if gameBoard[y + 2 + count][x] == p:
                    count += 1
                    for i in range(count):
                        gameBoard[y + 1 + i][x] = p
                    break
                else:
                    if gameBoard[y + 2 + count][x] == "." or gameBoard[y + 2 + count][x] == "#":
                        count = 0
                        break
                    else:
                        count += 1
        gameBoard[y][x] = p
        count = 0
        if x - 1 >= 0 and y - 1 >= 0 and gameBoard[y - 1][x - 1] != "." and gameBoard[y - 1][x - 1] != p and gameBoard[y - 1][x - 1] != "#":
            while (y - 2 - count >= 0) and (x - 2 - count >= 0):
                if gameBoard[y - 2 - count][x - 2 - count] == p:
                    count += 1
                    for i in range(count):
                        gameBoard[y - 1 - i][x - 1 - i] = p
                    break
                else:
                    if gameBoard[y - 2 - count][x - 2 - count] == "." or gameBoard[y - 2 - count][x - 2 - count] == "#":
                        count = 0
                        break
                    else:
                        count += 1
        gameBoard[y][x] = p
        count = 0
        if y - 1 >= 0 and x + 1 <= len(gameBoard) - 1 and gameBoard[y - 1][x + 1] != "." and gameBoard[y - 1][x + 1] != p and gameBoard[y - 1][x + 1] != "#":
            while (y - 2 - count >= 0) and (x + 2 + count <= len(gameBoard) - 1):
                if gameBoard[y - 2 - count][x + 2 + count] == p:
                    count += 1
                    for i in range(count):
                        gameBoard[y - 1 - i][x + 1 + i] = p
                    break
                else:
                    if gameBoard[y - 2 - count][x + 2 + count] == "." or gameBoard[y - 2 - count][x + 2 + count] == "#":
                        count = 0
                        break
                    else:
                        count += 1
        gameBoard[y][x] = p
        count = 0
        if y + 1 <= len(gameBoard) - 1 and x - 1 >= 0 and gameBoard[y + 1][x - 1] != "." and gameBoard[y + 1][x - 1] != p and gameBoard[y + 1][x - 1] != "#":
            while (y + 2 + count <= len(gameBoard) - 1) and (x - 2 - count >= 0):
                if gameBoard[y + 2 + count][x - 2 - count] == p:
                    count += 1
                    for i in range(count):
                        gameBoard[y + 1 + i][x - 1 - i] = p
                    break
                else:
                    if gameBoard[y + 2 + count][x - 2 - count] == "." or gameBoard[y + 2 + count][x - 2 - count] == "#":
                        count = 0
                        break
                    else:
                        count += 1
        gameBoard[y][x] = p
        count = 0
        if y + 1 <= len(gameBoard) - 1 and x + 1 <= len(gameBoard) - 1 and gameBoard[y + 1][x + 1] != "." and gameBoard[y + 1][x + 1] != p and gameBoard[y + 1][x + 1] != "#":
            while (y + 2 + count <= len(gameBoard) - 1) and (x + 2 + count <= len(gameBoard) - 1):
                if gameBoard[y + 2 + count][x + 2 + count] == p:
                    count += 1
                    for i in range(count):
                        gameBoard[y + 1 + i][x + 1 + i] = p
                    break
                else:
                    if gameBoard[y + 2 + count][x + 2 + count] == "." or gameBoard[y + 2 + count][x + 2 + count] == "#":
                        count = 0
                        break
                    else:
                        count += 1
        gameBoard[y][x] = p
        count = 0

# Pretty self explanatory

def has_valid_moves(gameBoard, p):
    count = 0
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard)):
            if gameBoard[i][j] == "." and valid_move(gameBoard, p, i, j, flip = False):
                count += 1
            else:
                continue
    
    if count > 0:
        return True
    else:
        return False

# This too

def has_empty_cells(gameBoard):
    count = 0
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard)):
            if gameBoard[i][j] == ".":
                count += 1
    
    if count >= 1:
        return True
    else:
        return False

# This calls the main function if the condition satisfies

if __name__ == "__main__":
    main()

# I was struggling more on Question 2 than this
# P.S. Please make the final exam easy, I'm already failing discrete pretty bad