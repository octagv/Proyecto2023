from collections import deque
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

def TableToList(table):
    columns = len(table[0])
    exit = deque()
    for row in table:
        for column in row:
            exit.append(column)
    for i in range(columns):
        exit.popleft()
    return list(exit)


