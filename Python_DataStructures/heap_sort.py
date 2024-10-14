# Heap Sort
# uses a data structure called a heap

# Time Complexity
# Best case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n log n)
# Space Complexity: O(1)

def heapify(arr, n, i):
    largest = i #index as root
    left = 2*i+1 #left side index
    right = 2*i+2 #right side index

    #check if left side is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    #check if right is greatest than root
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    #change root when needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] #swapping
        #heapify
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 -1, -1, -1):
        heapify(arr, n, i)

    #extract
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] #swap
        heapify(arr, i, 0)

    return arr

#Usage
arr = [23, 13, 45, 57,8,90]
sorted_arr = heap_sort(arr.copy())
print(f"Array: {arr} \nHeap Sorted: {sorted_arr}")

# Advantages
# -- consistent O(n log n)
# -- in place sorting
# -- no worst case like quick sort

# DisAdvantages
# -- not stable sort
# -- less efficient