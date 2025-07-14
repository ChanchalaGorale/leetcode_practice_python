
# Level: Easy
# Title: 21. Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists

#Problem Summary:
#You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted linked list, and return the head of the new list.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach remaining nodes
        tail.next = list1 or list2

        return dummy.next

#Time and Space Complexity:
#Time: O(n + m) (n, m = lengths of the lists)
#Space: O(1)