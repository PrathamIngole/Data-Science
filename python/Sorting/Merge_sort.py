# merge sort algorithm is based on divide and conqure algorithm 

# defining merge function to merge divided arrays
def merge(arr, low, mid, high) :

    i = low
    j = mid+1

    # defining new array to store merge array
    res = []

    # adding elements into the res array 
    while i <= mid and j <= high :
        if arr[i] < arr[j] :
            res += [arr[i]]
            i += 1
        else :
            res += [arr[j]]
            j += 1

    
    # adding remaining first part element
    while i <= mid :
        res += [arr[i]]
        i += 1
    
    # adding remaining second part element
    while j <= high :
        res += [arr[j]]
        j += 1

    # assinging to the proper positions of the element into orriginal array 
    for i in range(len(res)) :
        
        # taking low + i cause in original array we only pass from low index so we need to assign fromm the respective index
        arr[i + low] = res[i]
    

def mergeSort(arr, low, high) :

    # base case : if ever low and high is same or by any chance if low get pass high imediately stop there
    if low >= high :
        return 

    # taking mid so that array can be devided into 2 parts : 1) is from low to mid 
                                                            # 2) is from mid + 1 to high 
    mid = (low + high) // 2
    mergeSort(arr, low, mid) 
    mergeSort(arr, mid+1, high) 

    # merging two array by sorting its array
    merge(arr, low, mid, high) 

   
arr = [8, 2, 5, 2, 9, 0, 1, 4, 7, 6, 3]

print("before sorting : ", arr) 

print("\n sorting please wait....")
mergeSort(arr, 0, len(arr)-1)

print("\nafter sorting array : ", arr)