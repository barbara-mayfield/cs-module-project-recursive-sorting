# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # Set pointers for each arr
    x = 0
    y = 0

    # Look through merged_arr
    for i in range(elements):
        print(merged_arr)

        if x < len(arrA) and y < len(arrB):
            # check which value is less
            if arrA[x] <= arrB[y]:
                # set the value in the list and increment the count for that list
                merged_arr[i] = arrA[x]
                x += 1
            else:
                merged_arr[i] = arrB[y]
                y += 1
        # check for one array to have all els
        elif x < len(arrA) and y is len(arrB):
            merged_arr[i] = arrA[x]
            x += 1
        else:
            merged_arr[i] = arrB[y]
            y += 1
    return merged_arr

# arr1 = [1, 2, 3]
# arr2 = [6, 5, 4]

# arr3 = merge(arr1, arr2)

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):

    # Your code here
    # Base Case. A list of 0 or 1 elements is sorted, by definition.
    if len(arr) > 1:
        # set midpoint
        mid = len(arr) // 2

        # split the list in two
        a = arr[:mid]
        b = arr[mid:]

        # halve until down to 1 item in both sublists
        a = merge_sort(a)
        b = merge_sort(b)

        # use the merge helper function to merge lists
        return merge(a, b)
    return arr

# print(merge_sort(arr3))


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
