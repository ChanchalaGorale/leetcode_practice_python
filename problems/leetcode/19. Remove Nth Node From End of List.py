
# Level: Medium
# Title: 19. Remove Nth Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list

#Problem Summary:
#Given the head of a linked list, remove the n-th node from the end of the list and return its head.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Move fast pointer n+1 steps ahead (to maintain a gap of n)
        for _ in range(n + 1):
            fast = fast.next

        # Move both fast and slow together until fast hits end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the n-th node from end
        slow.next = slow.next.next

        return dummy.next
    

#Time and Space Complexity:
#Time: O(L) where L is the number of nodes in the list
#Space: O(1) — only uses constant extra space