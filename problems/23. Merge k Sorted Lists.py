
# Level: Hard
# Title: 23. Merge k Sorted Lists
# Link: https://leetcode.com/problems/merge-k-sorted-lists

#Problem Summary:
#You are given an array of k linked lists, each list is sorted in ascending order. Merge all the linked lists into one sorted linked list and return it.


from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # For easier debugging
    def __repr__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Step 1: Initialize the heap with the head of each list
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))  # Use (value, idx, node) to avoid comparing ListNode directly

        dummy = ListNode(0)
        current = dummy

        # Step 2: Pop the smallest node and push its next into the heap
        while heap:
            val, idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return dummy.next

#Time and Space Complexity:
#Time: O(N log k)
#Space: O(k+1)
