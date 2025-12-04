def  readInpText(filename):
    fileContent = open(filename, 'r')
    return fileContent.readlines()

def countRolls(pattern):
    count = 0
    for row in range(len(pattern)):
        pattern[row] = pattern[row].strip()
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
                    #print(row, col)
                    count += 1
    
    return count

pattern = readInpText('inp.txt')
print(countRolls(pattern))
                
''''
00 01 02
10 11 12
20 21 22
'''
