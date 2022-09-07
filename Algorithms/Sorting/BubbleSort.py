def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j+ 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    return arr

def main():
    arr = [7, 3, 1, 8, 9, 4, 5, 6, 10, 2]
    print(f"Original array: {arr}")
    sorted_arr = bubble_sort(arr)
    print(f"Sorted array: {sorted_arr}")

main()