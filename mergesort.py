def mergesort(arr, l, r):
    mid = (l -r)//2
    if (l-r <= 0):
        return
    elif (r-l > 1):
        mergesort(arr, l, mid)
        mergesort(arr, mid+1, r)
    merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    a = mid- l + 1
    b = r - mid

    L = arr[l:mid]  # copying left side of array
    R = arr[mid:r]  # copying right side of array

    left_counter = 0
    right_counter = 0 
    arr_counter = l
    while (left_counter < a and right_counter < b): #comparing elements from each array progressively
        if (L[left_counter] < R[right_counter]):
            arr[arr_counter] = L[left_counter]
            left_counter += 1
        elif (L[left_counter] > R[right_counter]):
            arr[arr_counter] = R[right_counter];
            right_counter += 1

        arr_counter += 1
    
    while (left_counter < a):    #copying leftovers from left array
        arr[arr_counter] = L[left_counter]
        arr_counter += 1
        left_counter += 1

    while (right_counter < b):    #copying leftovers from right array
        arr[arr_counter] = R[right_counter]
        arr_counter += 1
        right_counter += 1