def countSort(arr, pos) :
    res = [0] * len(arr) 
    count = [0] * 10
     
    for i in arr :
        index = (i//pos) % 10
        count[index] += 1
    
    for i in range(1, len(count)) :
        count[i] += count[i-1]

    
    for i in range(len(arr)-1, -1, -1) :
        index = (arr[i]//pos) % 10
        res[count[index] - 1] = arr[i]
        count[index] -= 1
    
    for i in range(len(arr)) :
        arr[i] = res[i]



def radixSort(arr) : 
    maxEle = arr[0]

    for i in arr : 
        if i > maxEle :
            maxEle = i

    pos = 1
    while maxEle :
        countSort(arr, pos) 
        pos *= 10
        maxEle //= 10

    return arr


print("sorted array is : ", radixSort([50, 318, 76, 0, 25, 676]))
