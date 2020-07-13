# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # Base Case - Start greater or equal to end
    if end >= start:
        # get the midpoint
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        # if target is less than mid, it's to the left
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)

        # if target is greater or equal to mid, it's to the right
        else:
            return binary_search(arr, target, mid + 1, end)
    else:
        return -1  # not found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here
