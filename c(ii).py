import random


def insertionsort(arr, start, end, key_comparisons):
    if end - start <= 0:  # trivially sorted in this case
        return 0

    for i in range(start + 1, end + 1):
        key = arr[i]  # key being inserted

        j = i - 1
        while j >= start:
            if key < arr[j]:
                key_comparisons += 1
                arr[j + 1] = arr[j]
                j -= 1
            else:
                key_comparisons += 1
                break

        arr[j + 1] = key
    return key_comparisons


def hybridsort(arr, start, end, key_comparisons, s):
    if end - start + 1 <= s:
        x = insertionsort(arr, start, end, key_comparisons)
        return key_comparisons + x

    mid = int((start+end)/2)
    y = hybridsort(arr, start, mid, key_comparisons, s)
    z = hybridsort(arr, mid+1, end, key_comparisons, s)
    p = merge(arr, start, mid, end, key_comparisons)
    return key_comparisons + y + z + p


def merge(arr, start, mid, end, key_comparisons):
    a = start
    b = mid+1

    while a <= mid and b <= end:  # as long as a and b do not exceed these bounds, compare
        if arr[a] < arr[b]:  # do nothing if head of left list is smaller, just shift a
            a += 1
        elif arr[b] < arr[a]:  # if head of right list is smaller, shift elements from a, one place to the right
            key = arr[b]
            j = mid
            while j >= a:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            mid += 1  # mid has moved one place to the right
            a += 1  # and so has the pointer for a
            b += 1
        elif arr[a] == arr[b]:  # otherwise, if head of left list and right list are equal, shift head of right list in
            key = arr[b]
            j = mid
            a += 1
            while j >= a:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            mid += 1
            a += 1
            b += 1
        key_comparisons += 1

    return key_comparisons

# main


arrSize = 100000
boundedS = 100
for i in range(1, boundedS + 1):
    s = i
    num_repetitions = 5
    while num_repetitions > 0:
        arr = []
        for j in range(0, arrSize):
            arr.append(random.randint(1, arrSize))
        key_comparisons = hybridsort(arr, 0, arrSize - 1, 0, s)
        print(f"number of comparisons, {5 - num_repetitions + 1}th time: {key_comparisons}")
        num_repetitions -= 1
    print("==============================")
