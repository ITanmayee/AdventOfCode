def  readInpText(filename):
    fileContent = open(filename, 'r')
    return fileContent.readlines()

opList = readInpText('inp1.txt')
print()
def formNumbers(opList):
    nums = []
    for i in range(len(opList[-1])):
        num = ''
        for j in range(len(opList) - 1):
            #print(i, j)
            num += opList[j][i]
        nums.append(num)
    return nums

def removeSpaces(opList):
    opList= opList.strip().split(' ')
    #print(opList)
    blank = ''
    while blank in  opList:
        opList.remove(blank)
        #print(opList)
    return opList

opNums = formNumbers(opList)
operators = removeSpaces(opList[-1])

#print(opNums, operators)
def totalOperations(opNums, operators):
    opIndx = 0
    #print(opList)
    total, ans = 0, 0
    op = operators[opIndx]
    
    if op == '*':
        ans = 1
        
    for i in range(len(opNums)):
        if opNums[i].replace(' ', '') == '':
            opIndx += 1
            op = operators[opIndx]
            total += ans
            ans = 0
            if op == '*':
                ans = 1
        else:
            if op == '*':
                ans *= int(opNums[i].strip())
            else:
                ans += int(opNums[i].strip())
        #print('ans ', ans)
    total += ans
    return total

print((totalOperations(opNums, operators)))
