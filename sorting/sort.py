arr: list = [9, 1, 2, 7, 3]


def selection_sort():
    for i in range(0, len(arr) - 1):
        min_index: int = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


def bubble_sort():
    for i in range(0, len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


def insertion_sort():
    for i in range(1, len(arr)):
        new_val: int = arr[i]
        j = i - 1

        while j >= 0 and new_val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = new_val


def _partition(lower_bound: int, upper_bound: int):
    i = lower_bound - 1
    pivot = arr[upper_bound]

    for j in range(lower_bound, upper_bound):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[upper_bound] = arr[upper_bound], arr[i + 1]
    return i + 1


def quick_sort(lower_bound: int, upper_bound: int):
    if lower_bound < upper_bound:
        partition_index = _partition(lower_bound, upper_bound)
        quick_sort(lower_bound, partition_index)
        quick_sort(partition_index, upper_bound)
