def is_unique(arr):
    """Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?"""
    if len(arr) == 1:
        return True
    if not arr:
        return True
    pivot = arr[-1]
    p_arr = [i for i in arr if i == pivot]
    if len(p_arr) > 1:
        return False
    lesser = [i for i in arr if i < pivot]
    greater = [i for i in arr if i > pivot]
    return is_unique(lesser) and is_unique(greater)

