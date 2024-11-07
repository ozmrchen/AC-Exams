# quick-sort.py
def quick_sort(arr):
    """
    Implementation of QuickSort algorithm.
    This uses the first element as pivot.
    """
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the first element as pivot
    pivot = arr[0]
    
    # Partition elements into less than, equal to, and greater than pivot
    less = []
    equal = []
    greater = []
    
    # Partition the array
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    
    # Recursively sort less and greater partitions, then combine all parts
    return quick_sort(less) + equal + quick_sort(greater)

# demonstration
data = [59, 67, 44, 73, 56, 84, 75, 62, 65, 71]
sorted_data = quick_sort(data)
print(data)
