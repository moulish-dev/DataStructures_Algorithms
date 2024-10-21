# SEARCHING ALGORITHMS

# used to search element in list or array

# Linear Search
# # checks each element seqentially
# Best Case: O(1) {target element in beginning}
# Average Case: O(n)
# Worst Case: O(n)
# Space Complexity: O(1)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  #target found
    return -1  #if target not found

#in efficient for large datasets

# Binary Search
#repeatedly divides and finds the target

# Best Case: O(1) {if target in middle}
# Average Case: O(log n)
# Worst Case: O(log n)
# Space Complexity: O(1)  ,,,, O(log n) if recursive used

#list should be already sorted
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low <= high:
        mid = (low+high) // 2
        #check middle
        if arr[mid] == target:
            return mid
        elif arr[mid] > target: #target is smaller than mid
            high = mid-1
        else:
            low = mid+1 #target is higher than mid
    return -1 #target not found

list=[1,2,4,2,4,2,6,45,34,23]
print(linear_search(list,1))
list.sort()
print(binary_search(list,1))

#requires sorting before
# time - efficient
# for large datasets