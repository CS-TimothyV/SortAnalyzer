# SORT ANALYZER STARTER CODE

import time
from math import floor

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS


def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")


# FUNCTIONS

def sortTimed(arrayIn, sorter):
    array = arrayIn.copy()
    start = getTime()
    sorter(array)
    end = getTime()
    if not sorted(array):
        raise Exception("Array not sorted!")
    return end - start


def getTime():
    return floor(time.time() * 1000)


def bubbleSort(arr):
    for passNum in range(len(arr)-1):
        for i in range(len(arr)-passNum-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


def selectionSort(arr):
    for start in range(len(arr)-1):
        min = start
        for search in range(start+1, len(arr)):
            if arr[search] < arr[min]:
                min = search
        arr[min], arr[start] = arr[start], arr[min]


def insertionSort(arr):
    for index in range(1, len(arr)):
        value = arr[index]
        insert = index
        while insert > 0 and arr[insert-1] > value:
            arr[insert] = arr[insert-1]
            insert -= 1
        arr[insert] = value


def sorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l) - 1))


for array in [["RANDOM", randomData], ["REVERSED", reversedData], ["NEARLY SORTED", nearlySortedData], ["FEW UNIQUE", fewUniqueData]]:
    print(f"\n>> {array[0]}")

    for sorter in [["BUBBLE", bubbleSort], ["SELECTION", selectionSort], ["INSERTION", insertionSort]]:
        results = []
        print("|")
        for i in range(20):
            print(f"| {sorter[0]}  {i+1}/20", end="\r")
            results.append(sortTimed(array[1], sorter[1]))

        print(f"| {sorter[0]}  Done!")
        sum = 0
        for result in results:
            print(f"|| {result}ms")
            sum += result
        print(f"|| Average: {sum/len(results)}ms")
