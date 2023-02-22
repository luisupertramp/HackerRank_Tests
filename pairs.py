
def pairs(k, arr):
    # arr.sort()
    # arr.reverse()

    # timesMatch = 0

    for i, number in enumerate(arr):

        #***** Here is one soltion I came up with : *****
        # nextPos = 1
        # # if we are not in the last position:
        # if i < len(arr)-1:  
        #     x = arr[i+nextPos]
        #     dif = number - x
        #     # iterate only from the current 'number' to the end until the difference is less than K
        #     while dif <= k :
        #         if dif == k :
        #             timesMatch += 1
                
        #         if nextPos+i+1 <= len(arr)-1 :
        #             nextPos += 1
        #             x = arr[i+nextPos]
        #             dif = number - x
        #         else : 
        #             # if there are not more elements to substract, dif is more than K so we can exit the while loop
        #             dif = k+1
        
        # ***** Another solution, more elefant but less efficient *****
        # if i < len(arr)-1:
        #     for j in range(i+1, len(arr)):
        #         if number-arr[j] == k :
        #             timesMatch += 1

        # ***** The brilliant solution that I found in a forum *****
        unique= set(arr)
        timesMatch=0
        for a in arr:
            if (a+k) in unique:
                timesMatch+=1
        return timesMatch

    
    # print(timesMatch)

print(pairs(2, [1, 5, 3, 4, 2]))