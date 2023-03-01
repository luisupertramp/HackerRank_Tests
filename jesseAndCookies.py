import heapq

def cookies(k, A):
    counter = 0
    
    heapq.heapify(A)
    
    while A[0] < k :
        
        if A[0] <= 0 :
            return -1
        
        if (len(A) == 1) and A[0] < k :
            return -1
    
        newElement = A[0] + (A[1]*2)
        heapq.heappop(A)
        heapq.heappushpop(A, newElement)
        counter += 1
        
    return(counter)


print(cookies(3581, [6214, 8543, 9266, 1150, 7498, 7209, 9398, 1529, 1032, 7384, 6784, 34, 1449, 7598, 8795, 756, 7803, 4112, 298, 4967, 1261, 1724, 4272, 1100, 9373]))