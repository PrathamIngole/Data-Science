def binarySearch(arr, key) :
    start = 0
    end = len(arr) - 1

    # search for element while start is less than end
    while start <= end :
        # calculate mid value 
        mid = (start + end) // 2

        # if mid value is the key then return it
        if arr[mid] == key :
            return "element found at index : ", mid
        # if key is smaller than middle value then modify end by end = mid - 1
        elif key < arr[mid] :
            end = mid - 1
        # if key is greater than middle value then modify end by start = mid + 1
        elif key > arr[mid] :
            start = mid + 1
        
    # if element not found on the iterator then return "element not found"
    return "element not found"

arr = [2, 6, 8, 33, 56, 89, 101]
key = 101

print(binarySearch(arr, key))