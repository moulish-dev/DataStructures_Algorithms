# Insertion Sort
# sorts each element one at a time

# Time and Space Complexity
# Best Case: O(n) (when the list is already sorted)
# Average Case: O(n²)
# Worst Case: O(n²)
# Space Complexity: O(1) (in-place sorting)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(i)
        #move one step if element is greater than key
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#Usage
arr = [23, 56, 34, 76, 46, 5]
sorted_arr = insertion_sort(arr.copy())
print("Array",arr)
print("Insertion sort: " ,sorted_arr)


# # Advantages
# -- good for small dataset
# -- simple
# -- maintains relative order of equal elements

# Disadvantages
# -- inefficient for large datasets
# -- large time complexity for random order lists
