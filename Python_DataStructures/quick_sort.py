# Quick Sort
# divide and conquer algorithm
# chooses a pivot(main) element and then makes sublists
# then recursively sorts it

# Time and Space Complexity
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n^2)
# Space Complexity: O(log n)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2] #selecting middle as pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    

#Usage
arr = [56, 23, 10, 5, 78, 34]
sorted_arr = quick_sort(arr.copy())
print(f"Array: {arr} \nQuick Sorted: {sorted_arr}")

# Advantages
# -- faster in practice (Mostly O(n log n))
# -- good for large datasets
# -- in-place sorting

# DisAdvantages
# -- O(n^2)
# -- not stable

