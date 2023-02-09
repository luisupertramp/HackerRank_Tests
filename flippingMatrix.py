
def flippingMatrix(matrix) :

    n = int(len(matrix)/2)

    maxQuadrants = []
    for i in range(n):
        for j in range(n):
            tempQuadrant = []
            tempQuadrant.append(matrix[i][j])
            tempQuadrant.append(matrix[i][len(matrix)-1-j])
            tempQuadrant.append(matrix[len(matrix)-1-i][j])
            tempQuadrant.append(matrix[len(matrix)-1-i][len(matrix)-1-j])
            maxQuadrants.append(max(tempQuadrant))
    
    # print(maxQuadrants)

    # print('Final sum: ')
    print(sum(maxQuadrants))


flippingMatrix([[112, 42, 83, 119],
                [56, 125, 56, 49],
                [15, 78, 101, 43],
                [62, 98, 114, 108]])

flippingMatrix([[1,2, 3, 4, 29,30],
                [5,6, 7, 8, 31,32],
                [9,10,11,12,33,34],
                [13,14,15,16,35,36],
                [17,18,19,20,21,22],
                [23,24,25,26,27,28]])

flippingMatrix([[1,2],
                [5,6]])