from Modules.Swap import swap


def InsertionSort(array):
    for i in range(1, len(array)):
        j = i
        while (j > 0) and (array[j] < array[j - 1]):
            swap(array, j, j - 1)
            j = j - 1
            yield array
