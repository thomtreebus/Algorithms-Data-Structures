def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def main():
    arr = [3, 8, 9, 10, 5, 34, 2, 6]
    index = linear_search(arr, 9)
    
    if index != -1:
        print(f"Target number found at index: {index}.")
    else:
        print("Target number not found.")

main()
