def linearSearch(arr, key) :

    # traverse whole array to find the key element
    for i in range(len(arr)) :

        # if you found the element return its index
        if key == arr[i] :
            return "element found at index : ", i
    
    # if not found return "element not found"
    return "Element not found"


arr = [34, 56, 2, 0, 23, 55, 20]


key = 55

print(linearSearch(arr, key))