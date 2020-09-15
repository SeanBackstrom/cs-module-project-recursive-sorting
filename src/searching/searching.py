# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    if end >= 1:
        mid = start + end // 2

        #if it is middle
        if arr[mid] == target:
            return mid

        #if its greater it can only be in left
        elif arr[mid] > target:
            #recurse the function except as only the left
            return binary_search(arr, target, start, mid-1)

        else:
            #put mid in start so it goes right
            return binary_search(arr, target, mid+1, end)

    else:
        # target is not present
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target, start, end):
 pass
    