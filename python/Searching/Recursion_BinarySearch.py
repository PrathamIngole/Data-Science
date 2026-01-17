def binarySearch(arr, key, start, end) :
    if start >= end :
        return "element not found"
    
    mid = (start + end) // 2
    if arr[mid] == key :
        return "element found at index : ", mid
    elif key > arr[mid] :
        return binarySearch(arr, key, mid+1, end)
    elif key < arr[mid] :
        return binarySearch(arr, key, start, mid - 1) 

arr = [1, 4, 6, 13, 22, 53, 100]
key = 13

print(binarySearch(arr, key, 0, len(arr) - 1))