"""
An imminent hurricane threatens the coastal town of Codeville.'
If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three.
"""

def rescue(weights, k):
    weights.sort()
    left, right = 0, len(weights) - 1
    boats = 0


    while left <= right:
        if weights[left] + weights [right] <= k:
            left += 1 # pair the lightest with heaviest
        right -= 1
        boats += 1 

    return boats

weights = [100, 500, 150, 80]
k = 200

print (rescue(weights,k))