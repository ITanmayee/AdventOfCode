def  readInpText(filename):
    fileContent = open(filename, 'r')
    return fileContent.readlines()

def countandRemoveRolls(pattern):
    count = 0
    updateRollIndx = []
    for row in range(len(pattern)):
        for col in range(len(pattern[row])):
            if pattern[row][col] == '@':
                adjRollCount = 0
                if row - 1 in range(len(pattern[row])) and col - 1 in range(len(pattern[row])):
                    if pattern[row-1][col-1] == '@':
                        adjRollCount += 1
                if row - 1  in range(len(pattern[row])) and col in range(len(pattern[row])):
                    if pattern[row-1][col] == '@':
                        adjRollCount += 1
                if row - 1 in range(len(pattern[row])) and col + 1 in range(len(pattern[row])):
                    if pattern[row-1][col+1] == '@':
                        adjRollCount += 1
                if row in range(len(pattern[row])) and col - 1 in range(len(pattern[row])):
                    if pattern[row][col-1] == '@':
                        adjRollCount += 1
                if row in range(len(pattern[row])) and col + 1 in range(len(pattern[row])):
                    if pattern[row][col+1] == '@':
                        adjRollCount += 1
                if row + 1 in range(len(pattern[row])) and col - 1 in range(len(pattern[row])):
                    if pattern[row+1][col-1] == '@':
                        adjRollCount += 1
                if row + 1 in range(len(pattern[row])) and col in range(len(pattern[row])):
                    if pattern[row+1][col] == '@':
                        adjRollCount += 1
                if row + 1 in range(len(pattern[row])) and col + 1 in range(len(pattern[row])):
                    if pattern[row+1][col+1] == '@':
                        adjRollCount += 1
                
                if adjRollCount < 4:
                    updateRollIndx.append((row, col))
                    count += 1
    
    return count, updateRollIndx 

def updatePattern(pattern, updateRollIndx):
    for (row, col) in updateRollIndx:
        pattern[row][col] = '.'
    return pattern

def countTurns(pattern):
    for row in range(len(pattern)):
        pattern[row] = [i for i in pattern[row].strip()]
    #print(pattern)
    adjRollCount, updateRollIndx = countandRemoveRolls(pattern)
    removeRolls = adjRollCount
    pattern = updatePattern(pattern, updateRollIndx)
    while adjRollCount != 0 :
        adjRollCount, updateRollIndx = countandRemoveRolls(pattern)
        removeRolls += adjRollCount
        pattern = updatePattern(pattern, updateRollIndx)
    return removeRolls

pattern = readInpText('inp.txt')
print(countTurns(pattern))
                
''''
00 01 02
10 11 12
20 21 22
'''
