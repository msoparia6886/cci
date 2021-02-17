def quicksort(arr):
    if len(arr) == 1:
        return arr
    if not arr:
        return []
    pivot = arr.pop(-1)
    lesser = [i for i in arr if i < pivot]
    greater = [i for i in arr if i > pivot]
    return quicksort(lesser) + [pivot] + quicksort(greater)
