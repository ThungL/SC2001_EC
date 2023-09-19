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
    # create temporary arrays, need only copy the left array, saves a bit on memory
    arr_left = []

    for i in range(start, mid + 1):
        arr_left.append(arr[i])

    size_l = len(arr_left)

    left_count = 0
    right_count = mid + 1
    arr_counter = start

    while left_count < size_l and right_count < end+1:
        if arr_left[left_count] == arr[right_count]:  # if both keys are equal, insert both at the same time
            arr[arr_counter] = arr_left[left_count]
            arr_counter += 1
            left_count += 1

            arr[arr_counter] = arr[right_count]
            arr_counter += 1
            right_count += 1

        elif arr_left[left_count] < arr[right_count]:
            arr[arr_counter] = arr_left[left_count]
            arr_counter += 1
            left_count += 1

        else:
            arr[arr_counter] = arr[right_count]
            arr_counter += 1
            right_count += 1

    # insert the remainder of the lists into the overall sorted list
    while left_count < size_l:
        for i in range(left_count, size_l):
            arr[arr_counter] = arr_left[i]
            arr_counter += 1
            left_count += 1

    while right_count < end+1:
        for i in range(right_count, end+1):
            arr[arr_counter] = arr[i]
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
