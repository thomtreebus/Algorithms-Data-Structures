def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr


def main():
    arr = [7, 3, 1, 8, 9, 4, 5, 6, 10, 2]
    print(f"Original array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array: {sorted_arr}")


main()