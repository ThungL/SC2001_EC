import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer

def generateRandomDatasets(array_size, array_max):
        arr = []
        for i in range(array_size):
            arr.append(random.randint(1, array_max))
        return arr


def insertionSort(arr):
    for i in range(1, len(arr)):
 
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

def mergesort(arr, l, r):
    if (l < r):
        mid = (l+r)//2
        mergesort(arr, l, mid)
        mergesort(arr, mid+1, r)

        merge(arr, l, mid, r)

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



def insertionTiming():
    insertion_timings = []
    print("STARTING INSERTION SORT TIMING")
    for x in range(1, 101):
        print("Starting timer for insert array size " + str(x))
        time = 0.0000000000
        for y in range(10000):
            arr = generateRandomDatasets(x, 1000)
            start = timer()
            insertionSort(arr)
            end = timer()
            time += (end-start)
        insertion_timings.append(time/10000)
    return insertion_timings
    
def mergeTiming():
    merge_timings = []
    print("STARTING MERGE SORT TIMING")
    for x in range(1, 101):
        print("Starting timer for insert array size " + str(x))
        time = 0.0000000000
        for y in range(10000):
            arr = generateRandomDatasets(x, 1000)
            start = timer()
            mergesort(arr, 0, x-1)
            end = timer()
            time += (end - start)
        merge_timings.append(time/10000)
    return merge_timings

def plotGraph(insertiontime, mergetime):
    x_axis = []
    for x in range(100):
        x_axis.append(x + 1)
    
    plt.plot(x_axis, insertiontime, label = 'insertion sort timing', color = "red")
    plt.plot(x_axis, mergetime, label='merge sort timing', color = "blue")
    plt.xlabel("array size")
    plt.ylabel("timing")
    plt.legend()
    plt.show()


insertion_timing = insertionTiming()
print(insertion_timing)
mergersort_timing = mergeTiming()
print(mergersort_timing)
plotGraph(insertion_timing, mergersort_timing)
