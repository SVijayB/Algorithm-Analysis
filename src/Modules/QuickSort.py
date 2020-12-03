from Modules.Swap import swap

def quicksort(array, low, high):
    if low >= high:
        return

    pivot = array[high]
    index = low

    for i in range(low, high):
        if array[i] < pivot:
            swap(array, i, index)
            index += 1
        yield array
    swap(array, high, index)
    yield array

    yield from quicksort(array, low, index - 1)
    yield from quicksort(array, index + 1, high)