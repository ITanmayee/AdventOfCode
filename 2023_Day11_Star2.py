'''
--- Part Two ---
The galaxies are much older (and thus much farther apart) than the researcher initially estimated.

Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.

(In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?

Your puzzle answer was 613686987427.
'''

def  readInpText(filename):
    fileContent = open(filename, 'r')
    return [line.strip() for line in fileContent.readlines()]

def getNoGalaxyRows(image):
    return [i for i in range(len(image)) if '#' not in image[i]]

def getNoGalaxyColsAndGalaxyPositions(image):
    total_cols = len(image[0])
    galaxyPositions = []
    noGalaxyCol = []
    for j in range(len(image)):
        count = 0
        for i in range(total_cols):
            if image[i][j] == '#':
                galaxyPositions.append((i, j))
                count += 1
        if count == 0:
            noGalaxyCol.append(j)
    return noGalaxyCol, galaxyPositions

def inSearchOfGalaxies(image):
    steps = 0
    noGalaxyRows = getNoGalaxyRows(image)
    noGalaxyCols, galaxyPositions = getNoGalaxyColsAndGalaxyPositions(image)
    for i in range(len(galaxyPositions)):
        for j in range(i + 1, len(galaxyPositions)):
            steps += abs(galaxyPositions[i][0] - galaxyPositions[j][0]) + abs(galaxyPositions[i][1] - galaxyPositions[
                j][1])
            for row in noGalaxyRows:
                min_row, max_row = min(galaxyPositions[i][0], galaxyPositions[j][0]), max(galaxyPositions[i][0],
                                                                                         galaxyPositions[j][0])
                if max_row >= row and min_row <= row:
                    steps += 999999
            for col in noGalaxyCols:
                min_col, max_col = min(galaxyPositions[i][1], galaxyPositions[j][1]), max(galaxyPositions[i][1],
                                                                                          galaxyPositions[j][1])
                if max_col >= col and min_col <= col:
                    steps += 999999
    return steps


myInp = readInpText('inp9.txt')
print(inSearchOfGalaxies(myInp))
