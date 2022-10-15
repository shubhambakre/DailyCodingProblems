# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the head of a singly linked list, swap every two nodes and return its head.
#
# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = ListNode(-1)
        current = head

        while(current and current.next):
            temp = current.val
            current.val = current.next.val
            current.next.val = temp
            current = current.next.next
        return head
