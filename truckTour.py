def truckTour(petrolpumps):
    pumps = petrolpumps.copy()
    totalPetrol = 0
    i = 0
    firstPump = 0

    while ((i < len(pumps)-1)) :
        totalPetrol += pumps[i][0]
        distance = pumps[i][1]
        firstPump = pumps[0]

        if distance > totalPetrol :
            pumps = pumps[i:] + pumps[:i]
            i=0
        else:
            i += 1
            totalPetrol -= distance

    print(pumps)
    return petrolpumps.index(firstPump)

# print(truckTour([[1, 5], [10, 3], [3, 4]]))
# truckTour([[10, 3], [3, 4], [1, 5]])
