s = int(input("S: "))
GLOBAL_THRESHOLD = s


def insertionsort(arr, start, end):
    if end - start <= 0:  # trivially sorted in this case
        return

    for i in range(start + 1, end + 1):
        key = arr[i]  # key being inserted

        j = i - 1
        while j >= start and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def hybridsort(arr, start, end):
    if end - start + 1 <= s:
        insertionsort(arr, start, end)
        return

    mid = int((start+end)/2)
    hybridsort(arr, start, mid)
    hybridsort(arr, mid+1, end)
    merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    # create temporary arrays
    arr_left = []
    arr_right = []
    for i in range(start, mid + 1):
        arr_left.append(arr[i])

    for i in range(mid + 1, end + 1):
        arr_right.append(arr[i])

    size_l = len(arr_left)
    size_r = len(arr_right)

    left_count = right_count = 0
    arr_counter = start

    while left_count < size_l and right_count < size_r:
        if arr_left[left_count] == arr_right[right_count]:  # if both keys are equal, insert both at the same time
            arr[arr_counter] = arr_left[left_count]
            arr_counter += 1
            left_count += 1

            arr[arr_counter] = arr_right[right_count]
            arr_counter += 1
            right_count += 1

        elif arr_left[left_count] < arr_right[right_count]:
            arr[arr_counter] = arr_left[left_count]
            arr_counter += 1
            left_count += 1

        else:
            arr[arr_counter] = arr_right[right_count]
            arr_counter += 1
            right_count += 1

    # insert the remainder of the lists into the overall sorted list
    while left_count < size_l:
        for i in range(left_count, size_l):
            arr[arr_counter] = arr_left[i]
            arr_counter += 1
            left_count += 1

    while right_count < size_r:
        for i in range(right_count, size_r):
            arr[arr_counter] = arr_right[i]
            arr_counter += 1
            right_count += 1

# main


arr = []
size_list = int(input("Number of elements: "))
print("Keys:")
for i in range(0, size_list):
    key = int(input())
    arr.append(key)
hybridsort(arr, 0, size_list - 1)
print(arr)
