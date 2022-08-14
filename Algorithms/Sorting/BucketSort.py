def bucket_sort(arr):
    buckets = [0 for i in range(len(arr) + 1)]
    sorted_arr = []
    
    for item in arr:
        buckets[item] += 1
    
    for value in range(len(buckets)):
        if buckets[value] > 0:
            for i in range(buckets[value]):
                sorted_arr.append(value)
    
    return sorted_arr


def main():
    arr = [7, 3, 1, 8, 9, 4, 5, 6, 10, 2]
    print(f"Original array: {arr}")
    sorted_arr = bucket_sort(arr)
    print(f"Sorted array: {sorted_arr}")

main()