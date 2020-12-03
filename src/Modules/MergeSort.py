def MergeSort(array, low, high):

    if high <= low:
        return

    mid = low + ((high - low + 1) // 2) - 1
    yield from MergeSort(array, low, mid)
    yield from MergeSort(array, mid + 1, high)
    yield from merge(array, low, mid, high)
    yield array

def merge(A, start, mid, end):
    merged = []
    left_index = start
    right_index = mid + 1

    while left_index <= mid and right_index <= end:
        if A[left_index] < A[right_index]:
            merged.append(A[left_index])
            left_index = left_index + 1
        else:
            merged.append(A[right_index])
            right_index = right_index + 1

    while left_index <= mid:
        merged.append(A[left_index])
        left_index = left_index + 1

    while right_index <= end:
        merged.append(A[right_index])
        right_index = right_index + 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A