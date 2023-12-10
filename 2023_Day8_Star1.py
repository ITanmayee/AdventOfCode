def getNodes(nodesInput):
    nodesList, connectingNodesList = [], []
    for nodeInfo in nodesInput:
        node, connectingNodes = nodeInfo.split(' = ')
        #print(node, connectingNodes)
        #nodeInfo = connectingNodes.split(', ')
        nodesList.append(node)
        #print(nodeInfo)
        connectingNodesList.append((connectingNodes[1:4], connectingNodes[-3:-6:-1]))
    # print('conn', connectingNodesList)
    return nodesList, connectingNodesList

def stepsToReachZZZ(instructions, nodesList, connectingNodesList):
    node = nodesList[0]
    left, right = connectingNodesList[0][0], connectingNodesList[0][1]
    instructionIndex, steps = 0, 1
    while node != 'ZZZ':
        print(node, left, right)
        if instructions[instructionIndex] == 'R':
            node = right
        else:
            node = left

        left, right = connectingNodesList[nodesList.index(node)][0], connectingNodesList[nodesList.index(node)][1]
        instructionIndex += 1
        if instructionIndex == len(instructions) - 1:
            instructionIndex = 0

        steps += 1
    return steps + 1

def readInpText(filename):
    fileContent = open(filename, 'r')
    return fileContent.readlines()

nodesList, connectingNodesList = getNodes(readInpText('inp11.txt'))
# print(nodesList, connectingNodesList)
print(stepsToReachZZZ('LLR', nodesList, connectingNodesList))
