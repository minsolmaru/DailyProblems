"""
Given a linked list, remove all consecutive nodes that sum to zero. 
Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. 
In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
"""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head

    prefix_sum = 0
    seen = {}

    curr = dummy
    while curr:
        prefix_sum += curr.val
        seen[prefix_sum] = curr
        curr = curr.next

    prefix_sum = 0
    curr = dummy
    while curr:
        prefix_sum += curr.val
        curr.next = seen[prefix_sum].next
        curr = curr.next

    return dummy.next
