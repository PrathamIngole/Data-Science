def CountSort(arr) : 
    # first we have to find which is the maximum elment in the array : 
    maxEle = arr[0]

    for i in range(len(arr)) :
        if arr[i] > maxEle :
            maxEle = arr[i]

    
    # now create one count array which is of size maximum : element + 1 and initialize it with "0"
    # count frequency of each element present in the originat array
    # output of this operation would be : 
    # [1, 2, 2, 1, 1, 2, 1, 0, 2]
    #  0  1  2  3  4  5  6  7  8
    count = [0] * (maxEle + 1)

    for i in arr : 
        count[i] += 1
    

    # modify count array for understanding the position by adding previous count from [1, last]
    # result would be : [1, 3, 5, 6, 7, 9, 10, 10, 12]

    for i in range(1, len(count)) :
        count[i] = count[i] + count[i-1] 
    
    
    # now we need new output array which is going to be our sorted array 
    res = [0] * len(arr)

    # for sorting array now we have to go reverse on original array so that we can place 
    # our formula --> first pick last element 
                    # then find that index at count array 
                    # reduce count by one at that index and then place that calculation index in output array 
                    # also reduce the count at that particular index at count array so that next time it will place different

    for i in range(len(arr)-1, -1, -1) :
        res[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return res


# dynamically taking size of the array and also the elements of the array : 

arr = [int(input(f"\nenter {i}th element : ")) for i in range(int(input("\nenter size of array : ")))]

# calling our count sort array : 
result = CountSort(arr) 

print("\nyour entered array is ", arr)

# result
print("\nsorted array is : ", result)


# ------------------------------------------------------------------------------------------------------------------------------

# OUTPUT Of the code is -

# enter size of array : 5

# enter 0th element : 0
# enter 1th element : 9
# enter 2th element : 4
# enter 3th element : 3
# enter 4th element : 7

# your entered array is  [0, 9, 4, 3, 7]

# sorted array is :  [0, 3, 4, 7, 9]