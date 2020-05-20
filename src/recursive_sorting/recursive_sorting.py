# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # loop through to the length of the merged array
    for i in range(len(merged_arr)):
        # if the two lists aren't empty
        if len(arrA) > 0 and len(arrB) > 0:
            # determine which value is greater, pop lower value to merged array
            if arrA[0] > arrB[0]:
                merged_arr[i] = arrB.pop(0)
            else:
                merged_arr[i] = arrA.pop(0)
        else:
            # if arrA is empty, add rest of arrB
            if len(arrA) == 0:
                merged_arr[i] = arrB.pop(0)
            else:
                merged_arr[i] = arrA.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    # Merges two subarrays of arr. 
    # First subarray is arr[l..m] 
    # Second subarray is arr[m+1..r] 
    # Inplace Implementation 

    start2 = mid + 1

    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return

    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end): 

        # If element 1 is in right place 
        if (arr[start] <= arr[start2]): 
            start += 1
        else: 
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): 
                arr[index] = arr[index - 1]
                index -= 1
            
            arr[start] = value

            # Update all the pointers 
            start += 1
            mid += 1
            start2 += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    if len(arr) <= 1:
        return arr

    if l < r:

        mid = (l + r) // 2

        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)

        merge_in_place(arr, l, mid, r)

    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
