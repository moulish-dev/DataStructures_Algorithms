# Selection Sort
# divides the input list into two - sorted and unsorted
# finds the minimum in the list and swaps with first element doing this again and again

# Time and Space Complexity
# Best Case: O(n^2)
# Average Case: O(n^2)
# Worst Case: O(n^2)
# Space Complexity: O(1)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        #assuming current holds minimum
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        #swap the found minimum with first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#Usage
arr = [34, 25, 7, 56, 64]
sorted_arr = selection_sort(arr.copy())
print(f"Array: {arr}")
print(f"Selection Sort: {sorted_arr}")

# Advantages
# --simple
# --good fo small dataset
# --no additional memory required

# DisAdvantages
# --ineffiecient for large datasets
# -- always O(n^2)