def getNodes(nodesInput):
    nodesList, connectingNodesList = [], []
    for nodeInfo in nodesInput:
        node, connectingNodes = nodeInfo.split(' = ')
        #print(node, connectingNodes)
        #nodeInfo = connectingNodes.split(', ')
        nodesList.append(node)
        #print(nodeInfo)
        connectingNodesList.append((connectingNodes[1:4], connectingNodes[-3:-6:-1][::-1]))
    # print('conn', connectingNodesList)
    return nodesList, connectingNodesList

def stepsToReachZZZ(instructions, nodesList, connectingNodesList):
    node = nodesList[0]
    instructionIndex, steps = 0, 0
    left, right = connectingNodesList[0][0], connectingNodesList[0][1]
    while True:
        if node == 'ZZZ':
                print('yes', left, right)
                break
        steps += 1
        if instructionIndex == len(instructions):
                instructionIndex = 0
        if instructions[instructionIndex] == 'R':
                node = right
        if instructions[instructionIndex] == 'L':
                node = left
        instructionIndex += 1
        #print(node, instructions[instructionIndex])  
        left, right = connectingNodesList[nodesList.index(node)][0], connectingNodesList[nodesList.index(node)][1]
        print(left, right)
    return steps

def readInpText(filename):
    fileContent = open(filename, 'r')
    return fileContent.readlines()

nodesList, connectingNodesList = getNodes(readInpText('aocd3inp.txt'))
print(nodesList, connectingNodesList)
print(stepsToReachZZZ('LRRLRRRLRLRLLRRLRLRLLRLRLRLLLLRRRLLRRRLRRRLRRRLLRLLRLRRLRLRLRRRLLLLRRLRLRRLRRLLRRRLRRLRLRRLRRLRRLRRLRLLRRLRRLLLLRLRLRRLLRRLLRRLRLLRLRRLRRLRRLRRRLRRLLLRRLRRRLRLRRRLLRLRRLRRRLRRLLRRRLRRLRLLRRLLRRLRRLRRRLRRLLRRLRRRLRLRLRLRLRLRRLRRLLRRRLRLRRLRRRLRLRLRLRLRLRRRLRRLRRRLLRRLRLLRRRLRRLRLLLLRRRLRRLRRRR', nodesList, connectingNodesList))
