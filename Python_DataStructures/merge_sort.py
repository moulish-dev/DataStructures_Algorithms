# Merge Sort
# divide and conquer algorithm
# divides list into smaller sublists and then arranges
# repeatedly merges the sublists

# Time and Space Complexity
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n log n)
# Space Complexity: O(n) additional space for merging

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 #middle of the array
        left = arr[:mid]    #left side of the arrau
        right = arr[mid:]   #right side of the array

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        #copy left and right arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i +=1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        #check if any element is left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

#Usage
arr = [54,67,3, 89, 26, 47]
sorted_arr = merge_sort(arr.copy())
print(f"Array: {arr} \n Merge Sorted: {sorted_arr} ")

#Advantages
# --consistent O(n log n) time complexity
# --stable sort
# --good for large datasets
# --good with linked lists

#DisAdvantages
# --requires additional memory
# --to be implemented with care


