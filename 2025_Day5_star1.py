def  readInpText(filename):
    fileContent = open(filename, 'r')
    return fileContent.readlines()

inp = readInpText('inp.txt')
#print(inp)
freshRanges = [i.strip().split('-') for i in inp[:inp.index('\n')]]

print(freshRanges)
freshRangesSum = len([int(i[1])- int(i[0]) + 1 for i in freshRanges])
print(freshRangesSum)
