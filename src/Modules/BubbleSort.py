from Modules.Swap import swap


def BubbleSort(array):
    if len(array) == 1:
        return
    switched = True
    for i in range(len(array) - 1):
        if not switched:
            break
        switched = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
                switched = True
            yield array
