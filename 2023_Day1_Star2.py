'''
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

Your puzzle answer was 53894.
'''

def getFirstDigit(txt):
    if txt[0] == 'o' and len(txt) >= 3 and txt[:3] == 'one':
        return '1'
    if txt[0] == 't':
        if len(txt) >= 3 and txt[:3] == 'two':
            return '2'
        if len(txt) >= 5 and txt[:5] == 'three':
            return '3'
    if txt[0] == 'f':
        if len(txt) >= 4 and txt[:4] == 'four':
            return '4'
        if len(txt) >= 4 and txt[:4] == 'five':
            return '5'
    if txt[0] == 's':
        if len(txt) >= 3 and txt[:3] == 'six':
            return '6'
        if len(txt) >= 5 and txt[:5] == 'seven':
            return '7'
    if txt[0] == 'e' and len(txt) >= 5 and txt[:5] == 'eight':
        return '8'
    if txt[0] == 'n' and len(txt) >= 4 and txt[:4] == 'nine':
        return '9'
    if txt[0] in '123456789':
        return txt[0]
    return getFirstDigit(txt[1:])


def getLastDigit(txt):
    if txt[-1] == 'e':
        if len(txt) >= 3 and txt[-3:] == 'one':
            return '1'
        if len(txt) >= 5 and txt[-5:] == 'three':
            return '3'
        if len(txt) >= 4 and txt[-4:] == 'five':
            return '5'
        if len(txt) >= 4 and txt[-4:] == 'nine':
            return '9'
    if txt[-1] == 'o':
        if len(txt) >= 3 and txt[-3:] == 'two':
            return '2'
    if txt[-1] == 'r' and len(txt) >= 4 and txt[-4:] == 'four':
        return '4'
    if txt[-1] == 'x' and len(txt) >= 3 and txt[-3:] == 'six':
        return '6'
    if txt[-1] == 'n' and len(txt) >= 5 and txt[-5:] == 'seven':
        return '7'
    if txt[-1] == 't' and len(txt) >= 5 and txt[-5:] == 'eight':
        return '8'
    if txt[-1] in '123456789':
        return txt[-1]
    return getLastDigit(txt[:-1])


def readInpText(filename):
    fileContent = open(filename, 'r')
    return fileContent.readlines()


def twoDigitCalibrationValue(txt):
    return int(getFirstDigit(txt) + getLastDigit(txt))


def CalibrationSum(InputTextList):
    return sum(map(twoDigitCalibrationValue, InputTextList))


myInp = readInpText('inp11.txt')
print(CalibrationSum(myInp))
