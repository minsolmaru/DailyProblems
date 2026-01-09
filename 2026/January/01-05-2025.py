"""
A girl is walking along an apple orchard with a bag in each hand. 
She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, 
determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.
"""

def longest_two_types(apples):
    from collections import defaultdict

    count = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(apples)):
        count[apples[right]] += 1

        while len(count) > 2:
            count[apples[left]] -= 1
            if count[apples[left]] == 0:
                del count[apples[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len







