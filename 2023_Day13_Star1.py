def readInpText(filename):
    fileContent = open(filename, 'r')
    return [line.strip() for line in fileContent.readlines()]

def getColumnPatterns(pattern):
    columnPatterns = []
    for i in range(len(pattern)):
        col = ''
        for j in range(len(pattern[0])):
            col += pattern[i][j]
    columnPatterns.append(col)
    return columnPatterns

def countReflections(patternLists):
    count = 0
    for i in range(len(patternLists)):
        for j in range(i+1, len(patternLists)):
            if patternLists[i] == patternLists[j]:
                count += 1
    return count


def findReflections(pattern):
    columns = getColumnPatterns(pattern)
    reflectedRows, reflectedCols = countReflections(pattern), countReflections(columns)
    print(reflectedRows, reflectedCols)
    # return steps


myInp = readInpText('inp9.txt')
print(myInp)
findReflections(myInp)
