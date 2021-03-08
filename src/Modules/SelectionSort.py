from Modules.Swap import swap


def SelectionSort(array):
    if len(array) == 1:
        return

    for i in range(len(array)):
        min_val = array[i]
        min_index = i
        for j in range(i, len(array)):
            if array[j] < min_val:
                min_val = array[j]
                min_index = j
            yield array
        swap(array, i, min_index)
        yield array
