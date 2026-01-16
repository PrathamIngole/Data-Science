def partition(arr, low, high) :
    pivot = arr[high]
    idx = low - 1
    
    for j in range(low, high) :
        if arr[j] <= pivot :
            idx += 1
            arr[j], arr[idx] = arr[idx], arr[j]
        
    idx += 1
    arr[idx], arr[high] = arr[high], arr[idx]

    return idx


def quicksort(arr, low , high) :
    if low >= high :
        return 
    
    pIndex = partition(arr, low, high)
    quicksort(arr, low, pIndex - 1) 
    quicksort(arr, pIndex + 1, high)



arr = [5, 2, 1, 7, 4]

print("before sorting array : ", arr)

quicksort(arr, 0, len(arr) - 1)

print("after sorting array : ", arr)

# OUTPUT :

# \python\Sorting>python Quick_Sort.py
# before sorting array :  [5, 2, 1, 7, 4]
# after sorting array :  [1, 2, 4, 5, 7]