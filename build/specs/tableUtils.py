def getRow(table, numRow):
    exitList = []
    index = len(table[0])
    for i in range(index):
        exitList.append(table[numRow][i])
    return exitList

def getColumn(table, numColumn):
    exitList = []
    index = len(table)
    for i in range(index):
        exitList.append(table[i][numColumn])
    return exitList

