def  readInpText(filename):
    fileContent = open(filename, 'r')
    return fileContent.readlines()

def findHighest(battery):
    battery = battery.strip()
    digit12 = []
    while True:  
        digits = sorted(([int(i) for i in battery]))
        while True and len(digits) > 0:
            highest = digits[-1]
            #print(highest)
            highestIndx = battery.index(str(highest))
            
            if len(battery[highestIndx + 1:]) >= 12 - len(digit12) - 1:
                digit12.append(str(highest))
                battery = battery[highestIndx + 1:]
                break
            else:
                digits = digits[:digits.index(highest)]
            #print(digits, highest, highestIndx, battery)
        if len(digit12) == 12:
            return int(''.join(digit12))

batteriesList = readInpText('inp.txt')
print(batteriesList)
print(sum(map(findHighest, batteriesList)))
