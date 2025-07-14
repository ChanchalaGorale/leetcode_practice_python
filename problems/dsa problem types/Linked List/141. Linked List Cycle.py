
# Level: Easy
# Title: 141. Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle

#Problem Summary:
#Given the head of a linked list, determine if the linked list has a cycle in it.

# A linked list has a cycle if any node in the list is visited more than once during traversal (i.e. there's a loop).

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
    

#Time and Space Complexity:
#Time: O(n)
#Space: O(1)