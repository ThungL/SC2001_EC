import random


GLOBAL_THRESHOLD_S = 10
key_comparisons = 0
arraySize = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
arr2sort = []

def generateRandomDatasets(array_size):
        arr = []
        for i in range(array_size):
            arr.append(random.randint(1, 99999999))
        return arr

def insertionsort(arr, start, end):
    global key_comparisons
    if end - start <= 0:  # trivially sorted in this case
        return

    for i in range(start + 1, end + 1):
        key = arr[i]  # key being inserted

        j = i - 1
        while j >= start and key < arr[j]:
            key_comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def hybridsort(arr, start, end):
    if end - start + 1 <= GLOBAL_THRESHOLD_S:
        insertionsort(arr, start, end)
        return

    mid = int((start+end)/2)
    hybridsort(arr, start, mid)
    hybridsort(arr, mid+1, end)
    merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    # create temporary arrays, need only copy the left array, saves a bit on memory
    global key_comparisons
    arr_left = []

    for i in range(start, mid + 1):
        arr_left.append(arr[i])

    size_l = len(arr_left)

    left_count = 0
    right_count = mid + 1
    arr_counter = start

    while left_count < size_l and right_count < end+1:
        if arr_left[left_count] == arr[right_count]:  # if both keys are equal, insert both at the same time
            key_comparisons += 1
            arr[arr_counter] = arr_left[left_count]
            arr_counter += 1
            left_count += 1

            arr[arr_counter] = arr[right_count]
            arr_counter += 1
            right_count += 1

        elif arr_left[left_count] < arr[right_count]:
            key_comparisons += 1
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


for i in arraySize:
    print("array size is :" + str(i))
    aveL = [0, 0, 0]
    for j in range(3):
        key_comparisons = 0
        arr2sort = generateRandomDatasets(i)
        hybridsort(arr2sort, 0, i - 1)
        aveL[j] = key_comparisons
        print("Key comparisons is : " + str(key_comparisons))

    ave = (aveL[0] + aveL[1] + aveL[2]) / 3
    print("Average number of key comparisons is")
    print(ave)
    print("\n")





