def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        print(f"middle: {middle}")
        if arr[middle] == target:
            return middle

        if arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1 
        
    return None

def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    index = binary_search(arr, 1)
    
    if index is not None:
        print(f"Target number found at index: {index}.")
    else:
        print("Target number not found.")

main()