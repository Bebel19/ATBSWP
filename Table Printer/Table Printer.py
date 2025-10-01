tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def  findLongestString(table):
    """

    :param table:
    :return: List of lengths of the longest string of each row of a table
    """


    longest = {
    "rowIndex" : 0,
    "cellIndex": 0,
    "length": 0,
    }

    res = []
    lengthsList = []

    for rowIndex, row in enumerate(table):
        for cellIndex, cell in enumerate(row):

            cellLength = len(cell)

            if cellLength > longest["length"]:

                longest["length"] = cellLength
                longest["rowIndex"] = rowIndex
                longest["cellIndex"] = cellIndex

        res.append(longest)
        longest = {
            "rowIndex": 0,
            "cellIndex": 0,
            "length": 0,
        }

    for dict in res:
        lengthsList.append(dict["length"])

    return lengthsList

def printTable(table):
    colWidths = [0] * len(table)

    lengthsList = findLongestString(table)
    longestLenght = max(lengthsList)

    for colIndex in range(len(table[0])):
        for lineIndex in range(len(colWidths)):
            print(f"{table[lineIndex][colIndex]}".center(longestLenght), end="\t")

        print("\n")




print(findLongestString(tableData))

printTable(tableData)
