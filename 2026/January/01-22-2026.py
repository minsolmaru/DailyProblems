"""
Given a array that's sorted but rotated at some unknown pivot, in which all elements are distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors. It is guaranteed that the first and last elements are lower than all others.
"""


def find_peak(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] < arr[mid + 1]:
            # Peak is to the right
            low = mid + 1
        else:
            # Peak is at mid or to the left
            high = mid

    return arr[low]  # or return low for index
