# selection-sort.py
def selection_sort(arr):
    """
    Implementation of Selection Sort algorithm.
    This sorts the array in-place.
    """
    # Create a copy to avoid modifying the original array
    arr = arr.copy()
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

# demonstration
data = [59, 67, 44, 73, 56, 84, 75, 62, 65, 71]
sorted_data = selection_sort(data)
print(data)