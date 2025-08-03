
# Level: Easy
# Title: 206. Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list

#Problem Summary:
#Given the head of a singly linked list, reverse the list and return the new head.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # save next
            curr.next = prev       # reverse pointer
            prev = curr            # move prev forward
            curr = next_node       # move curr forward

        return prev
    

#Time and Space Complexity:
#Time: O(n)
#Space: O(1)