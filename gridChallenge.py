def gridChallenge(grid):
    sortedGrid = []

    lenRows = len(grid)

    for row in grid :
        lenCols = len(row)
        sortedRow = list(row)
        sortedRow.sort()
        sortedGrid.append(sortedRow)
        # print(sortedRow)
    
    difRowsCols = 0
    if lenRows != lenCols : 
        difRowsCols = abs(lenRows - lenCols)

    transposedGrid = []
    for i in range(len(sortedGrid)-difRowsCols):
        tempRow = []
        for j in range(len(sortedGrid)):
            tempRow.append(sortedGrid[j][i])
        transposedGrid.append(tempRow)
        sortedRow = tempRow.copy()
        sortedRow.sort()

        if tempRow != sortedRow :
            return 'NO'
        # print (sortedRow)
        # print (tempRow)
    
    return 'YES'
        

# print(gridChallenge(['kc', 'iu']))
# print(gridChallenge(['uxf' , 'vof' , 'hmp']))
# print(gridChallenge(['abc' , 'lmp' , 'qrt']))
print(gridChallenge(['mpxz' , 'abcd' , 'wlmf']))
# print(gridChallenge(['abc' , 'hjk' , 'mpq' , 'rtv']))
# print(gridChallenge(['eibjbwsp', 'ptfxehaq', 'jxipvfga', 'rkefiyub', 'kalwfhfj', 'lktajiaq', 'srdgoros', 'nflvjznh']))