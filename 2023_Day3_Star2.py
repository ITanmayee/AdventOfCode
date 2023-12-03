'''
--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

Your puzzle answer was 82818007.
'''

def readInpText(filename):
    fileContent = open(filename, 'r')
    return fileContent.readlines()

def getNum(txt, digitIndex):
        num = txt[digitIndex]
        leftDigitsIndex = digitIndex - 1
        while leftDigitsIndex >= 0:
                if txt[leftDigitsIndex] in '0123456789':
                        num = txt[leftDigitsIndex] + num
                else:
                    break
                leftDigitsIndex -= 1
        rightDigitsIndex = digitIndex + 1
        while rightDigitsIndex < len(txt):
                if txt[rightDigitsIndex] in '0123456789':
                        num = num + txt[rightDigitsIndex]
                else:
                    break
                rightDigitsIndex += 1
        return int(num)

def isValidIndex(currentRow, currentCol, rows, cols):
        return currentRow >= 0 and currentRow < rows and currentCol >= 0 and currentCol < cols

def numbersSum(inputTextList):
        ans = 0
        rows, cols = len(inputTextList), len(inputTextList[0].strip())
        for line in range(rows):
                for ch in range(cols):
                        if inputTextList[line][ch] == '*':
                                numbers = []
                                if isValidIndex(line-1, ch-1, rows, cols) and inputTextList[line - 1][ch - 1] in '0123456789':
                                        numbers.append(getNum(inputTextList[line - 1], ch - 1))
                                if isValidIndex(line-1, ch, rows, cols) and inputTextList[line - 1][ch] in '0123456789':
                                        numbers.append(getNum(inputTextList[line - 1], ch))
                                if isValidIndex(line-1, ch+1, rows, cols) and inputTextList[line - 1][ch + 1] in '0123456789':
                                        numbers.append(getNum(inputTextList[line - 1], ch + 1))
                                if isValidIndex(line+1, ch-1, rows, cols) and inputTextList[line + 1][ch - 1] in '0123456789':
                                        numbers.append(getNum(inputTextList[line + 1], ch - 1))
                                if isValidIndex(line+1, ch, rows, cols) and inputTextList[line + 1][ch] in '0123456789':
                                        numbers.append(getNum(inputTextList[line + 1], ch))
                                if isValidIndex(line+1, ch+1, rows, cols) and inputTextList[line + 1][ch + 1] in '0123456789':
                                        numbers.append(getNum(inputTextList[line + 1], ch + 1))
                                if isValidIndex(line, ch-1, rows, cols) and inputTextList[line][ch - 1] in '0123456789':
                                        numbers.append(getNum(inputTextList[line], ch - 1))
                                if isValidIndex(line, ch+1, rows, cols) and inputTextList[line][ch + 1] in '0123456789':
                                        numbers.append(getNum(inputTextList[line], ch + 1))
                                gearPartlyNumbers = list(set(numbers))
                                if len(gearPartlyNumbers) == 2:
                                    ans += (gearPartlyNumbers[0] * gearPartlyNumbers[1])
        return ans
        
myInp = readInpText('day3inp11.txt')
print(numbersSum(myInp))
