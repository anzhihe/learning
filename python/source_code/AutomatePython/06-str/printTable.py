def getColWidth(table, widths):
    for i in range(len(table)):            
        colWidth = 0
        for item in table[i]:
            widths[i] = max(widths[i], len(item))
            

def printTable(table, widths):
    rowNum = len(table)
    colNum = len(table[0])
    for y in range(colNum):
        print(table[0][y].ljust(widths[0]), end=' ')
        for x in range(1, rowNum):
            print(table[x][y].ljust(widths[x]), end=' ')
        print()
    

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
colWidths = [0] * len(tableData)


getColWidth(tableData, colWidths)
printTable(tableData, colWidths)
