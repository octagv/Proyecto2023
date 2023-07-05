from collections import deque
import pandas as pd
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

def TableToDataFrame(table):
    return pd.DataFrame(table)

def DataFrameToTable(dataframe):
    table = []
    for i in range(dataframe.index[-1]+1):
        row_list = dataframe.loc[i, :].values.flatten().tolist()
        table.append(row_list)
    return table

if __name__ == "__main__":
     df = pd.DataFrame([["A","B","C"], [1,2,3], ["A","B","C"], [1,2,3]])

     print(DataFrameToTable(df))



