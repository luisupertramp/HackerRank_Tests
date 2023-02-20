def minimumBribes(q):
    # Write your code here
    bribes = 0
    tempQ = []
        
    tempQ = list(range(1,len(q)+1))
    print(tempQ)

    for i, person in enumerate(q):
        if person != tempQ[i]:
            tempPosition = tempQ.index(person) # where person is supposed to be
            if (tempPosition - i) < 3 :
                bribes += (tempPosition - i) # difference from where person is supposed to be - where it actually is
                tempQ = q[:i+1] + tempQ[i: tempPosition ] + tempQ[tempPosition+1:]
            else :
                print('Too chaotic')
                return
    
    print(bribes)

# minimumBribes([2, 5, 1, 3, 4])
# minimumBribes([2, 1, 5, 3, 4])
# minimumBribes([1,2,3,5,4,6,7,8,9])
# minimumBribes([5, 1, 2, 3, 7, 8, 6, 4])

# minimumBribes([1, 2, 3, 4, 5, 6, 7, 8])
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])

