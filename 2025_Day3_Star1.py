def  readInpText(filename):
    fileContent = open(filename, 'r')
    return fileContent.readlines()

def findMax(battery):
    battery = battery.strip()
    digits = sorted(([int(i) for i in battery]))
    max_digit= digits[-1]
    if battery.count(str(max_digit)) == 1 and battery[-1] == str(max_digit):
        dummy_battery = battery.replace(str(max_digit), '')
        max_digit = sorted(([int(i) for i in dummy_battery]))[-1]
    battery = battery[battery.index(str(max_digit)) + 1:]
    return int(str(max_digit) + str(sorted(([int(i) for i in battery]))[-1]))

batteriesList = readInpText('inp.txt')
print(batteriesList)
print(sum(map(findMax, batteriesList)))
