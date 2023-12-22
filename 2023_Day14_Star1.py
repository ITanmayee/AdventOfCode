def readInpText(filename):
    fileContent = open(filename, 'r')
    return [list(line.strip()) for line in fileContent.readlines()]

def findTopMostCubeRockRow(rocks, roundRockRow, column):
    for row in range(roundRockRow - 1, -1, -1):
        if rocks[row][column] == '#':
            return row
    return 0
def tiltRocksToNorth(rocks):
    #lastColumnIndex = len(rocks[0]) - 1
    topMostRowIndex = 0
    columnPatterns = []

    for i in range(len(rocks)):
        for j in range(len(rocks[0])):
            if rocks[i][j] == 'O':
                topMostCubeRockRow = findTopMostCubeRockRow(rocks, i, j)
                if topMostCubeRockRow == 0:
                    for row in range(i):
                        if rocks[row][j] == '.':
                            rocks[row][j], rocks[i][j] = rocks[i][j], rocks[row][j]
                            break
                else:
                    for row in range(topMostCubeRockRow, len(rocks)):
                        if rocks[row][j] == '.':
                            rocks[row][j], rocks[i][j] = rocks[i][j], rocks[row][j]
                            break
                printL(rocks)
                print()
                print()
                # print(i, j, findTopMostCubeRockRow(rocks, i, j))
    return rocks

def findLoad(rocks):
    load = 0
    for i in range(len(rocks)):
        for j in range(len(rocks[0])):
            if rocks[i][j] == 'O':
                load += (len(rocks) - i)
    return load

def printL(rocks):
    for i in rocks:
        print(''.join(i))

myInp = readInpText('inp14.txt')
# tiltRocksToNorth(myInp)
print(findLoad(tiltRocksToNorth(myInp)))
