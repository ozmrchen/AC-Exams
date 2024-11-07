def calculate_mean(numbers):
    """Calculate the arithmetic mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """Calculate the median of a list of numbers."""
    # Sort the list
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    
    # If length is odd, return middle number
    if length % 2 == 1:
        return sorted_numbers[length // 2]
    
    # If length is even, return average of two middle numbers
    middle_right = length // 2
    middle_left = middle_right - 1
    return (sorted_numbers[middle_left] + sorted_numbers[middle_right]) / 2

def calculate_mode(numbers):
    """Calculate the mode of a list of numbers."""
    # Create a dictionary to store frequency of each number
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Find the maximum frequency
    max_frequency = max(frequency.values())
    
    # Get all numbers that appear with maximum frequency
    modes = [num for num, freq in frequency.items() if freq == max_frequency]
    
    # If all numbers appear same number of times, return None
    if len(modes) == len(numbers):
        return None
    
    return modes

# Your data
numbers = [59, 67, 44, 73, 56, 84, 75, 62, 65, 71]

# Calculate statistics
mean = calculate_mean(numbers)
median = calculate_median(numbers)
mode = calculate_mode(numbers)

# Print results
print(f"Numbers: {numbers}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode if mode else 'No mode (all numbers appear once)'}")
