from arrays_and_strings import sorting

def is_unique(arr):
    """
    Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
    cannot use additional data structures?

    :param arr: Array (string is an array of characters) to check for unique elements.
    :returns: True if the all the elements in array/string are unique
    :rtype: bool
    """
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


def isUnique(array):
    """Anil find if array has duplicates"""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        if len(equal) > 1:
            return False
        return isUnique(less) and isUnique(greater)
    else:
        return True


def check_permutations(str1, str2):
    """
    Given two strings, write a method to decide if one is a permutation of the
    other.

    :param str1: One of two strings to check if it is a permutation of another
    :param str2: One of two strings to check if it is a permutation of another
    :returns: True if one of the two strings is a permutation of another
    :rtype: bool
    """

    stack = sorting.quicksort(list(str1))
    for c in str2:
        try:
            stack.remove(c)
        except ValueError:
            return False
    if len(stack) > 0:
        return False
    return True


def palindrome_permutations(in_str):
    """
    Given a string, write a function to check if it is a permutation of a palindrome.
    A palindrome is a word or phrase that is the same forwards and backwards. A permutation
    is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

    :param in_str: Input string to check for palindrome permutations e.g. "tact coa"
    :returns: True if the given string has pertubations that are palindrome e.g. ["taco cat", "atco eta"]
    """

    sorted_str = ''.join(sorting.quicksort(list(in_str))).lstrip(' ')
    i = 0
    tmp = list()
    while i < len(sorted_str):
        try:
            if sorted_str[i] == sorted_str[i+1]:
                i += 1
            else:
                tmp.append(sorted_str[i])
        except IndexError:
            tmp.append(sorted_str[i])
        i += 1
    if len(tmp) > 1:
        return False
    else:
        return True

