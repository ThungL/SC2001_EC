import random
import time

GLOBAL_THRESHOLD_S = 74
key_comparisons = 0
arraySize = 10000000
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

def mergesort(arr, start, end):
    if start < end:
        mid = int((start+end)/2)
        mergesort(arr, start, mid)
        mergesort(arr, mid+1, end)
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

HSList = []
MSList = []
HStList = []
MStList = []

print("array size is :" + str(arraySize))
HSaveL = [0, 0, 0, 0, 0]
MSaveL = [0, 0, 0, 0, 0]
HStimeTakenList = [0, 0, 0, 0, 0]
MStimeTakenList = [0, 0, 0, 0, 0]

for j in range(5):
    key_comparisons = 0
    arr2hybridsort = generateRandomDatasets(arraySize)
    arr2mergesort = arr2hybridsort.copy()
    print("Test" + str(j+1))
    #print(arr2hybridsort)
    #print("\n \n \n")
    HSstart = time.time()
    hybridsort(arr2hybridsort, 0, (arraySize - 1))
    HSend = time.time()
    HStimeTaken = HSend-HSstart
    HSaveL[j] = key_comparisons
    HStimeTakenList[j] = HStimeTaken
    print("HS done : " + str(j+1))
    # print("Key comparisons is : " + str(key_comparisons))
    # print(arr2hybridsort)
    # print("\n \n \n")
    # print(arr2mergesort)
    # print("\n \n \n")
    key_comparisons = 0
    MSstart = time.time()
    mergesort(arr2mergesort, 0, (arraySize - 1))
    MSend = time.time()
    MStimeTaken = MSend - MSstart
    MSaveL[j] = key_comparisons
    MStimeTakenList[j] = MStimeTaken
    print("MS done : " + str(j+1))
    # print(arr2mergesort)
    # print("\n \n \n")

HSave = (HSaveL[0] + HSaveL[1] + HSaveL[2] + HSaveL[3] + HSaveL[4]) / 5
HSaveTimeTaken = (HStimeTakenList[0] + HStimeTakenList[1] + HStimeTakenList[2] + HStimeTakenList[3] + HStimeTakenList[4]) / 5
MSave = (MSaveL[0] + MSaveL[1] + MSaveL[2] + MSaveL[3] + MSaveL[4]) / 5
MSaveTimeTaken = (MStimeTakenList[0] + MStimeTakenList[1] + MStimeTakenList[2] + MStimeTakenList[3] + MStimeTakenList[4]) / 5

print("HybridSort average key comparison = " + str(HSave))
print("MergeSort average key comparison = " + str(MSave))
print("\n")
print("HybridSort average time taken = " + str(HSaveTimeTaken))
print("MergeSort average time taken = " + str(MSaveTimeTaken))

# print("Average number of key comparisons is")
# print(ave)
# print("\n")
# sList.append(HSave)
# tList.append(aveTimeTaken)

# print(sList) #print out list of ave, list of array size can be seen at the start
# print(tList) #print out list of time taken ave
