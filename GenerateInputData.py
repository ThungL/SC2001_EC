import array
import random

def generateRandomData(ArrSize, largestNum):
    arr = [1]
    for x in range(ArrSize-2):
        arr.append(random.randint(0, largestNum))
    arr.append(largestNum)
    return arr


arraySize = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
largestNum = 999999999
inputData = generateRandomData(arraySize[0], largestNum)
for x in inputData:
    print(x)
#can then use inputData to use for merge/insertion/hybrid