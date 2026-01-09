"""
You are given a list of N numbers, in which each number is located at most k places away from its sorted position. 
For example, if k = 1, a given element at index 4 might end up at indices 3, 4, or 5.

Come up with an algorithm that sorts this list in O(N log k) time.
"""

import heapq

def sort_k_sorted(arr, k):
    heap = arr[:k+1]
    heapq.heapify(heap)

    index = 0

    for i in range(k+1, len(arr)):
        arr[index] = heapq.heappop(heap)
        index += 1
        heapq.heappush(heap, arr[i])

    while heap:
        arr[index] = heapq.heappop(heap)
        index += 1

    return arr
