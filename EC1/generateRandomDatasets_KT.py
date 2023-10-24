arraySize = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]

arr2sort = []

def generateRandomDatasets(array_size):
        arr = []
        for i in range(array_size):
            arr.append(random.randint(1, array_size))
        return arr

for i in arraySize:
    arr2sort = generateRandomDatasets(i)

# ^ an example of how to use
