# Bubble Sort
# compares adjacent elements and swaps them to sort it

# Time and Space Complexity
# Best Case : O(n)  -- list is already sorted
# Average Case : O(n^2)
# Worst Case: O(n^2)
# Space Complexity: O(1)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  #track if swap happens
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                #swap if in wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            # array is sorted
            break
    return arr

#Usage
arr=[23,3,56,67,78,1,8]
sorted_arr = bubble_sort(arr.copy())
print(f"Array:{arr}")
print(f"Sorted Array : {sorted_arr}")

# Advantages
# -- simple 
# -- doesn't require extra memory

# # DisAdvantages
# -- inefficient for large datasets
# -- high time complexity