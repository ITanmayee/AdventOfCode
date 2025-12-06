
def  readInpText(filename):
    fileContent = open(filename, 'r')
    return fileContent.readlines()

opList = readInpText('inp1.txt')

def removeSpaces(opList):
    for i in range(len(opList)):
        opList[i] = opList[i].strip().split(' ')
        #print(opList)
        blank = ''
        while blank in  opList[i]:
            opList[i].remove(blank)
            #print(opList)
    return opList

def totalOperations(opList):
    print(opList)
    total = 0
    for i in range(len(opList[-1])):
        op = opList[-1][i]
        ans = 0
        if op == '*':
            ans = 1
        for x in range(len(opList) - 1):
            if op == '*':
                ans *= int(opList[x][i])
            else:
                 ans += int(opList[x][i])
        
        total += ans
    return total

print(totalOperations(removeSpaces(opList)))
