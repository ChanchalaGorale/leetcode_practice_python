# Level: Hard
# Title: 1298. Maximum Candies You Can Get from Boxes
# Link: https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

#Problem Summary:
# You are given:
# status[i]: 1 if the i-th box is open, else 0.
# candies[i]: number of candies in the i-th box.
# keys[i]: list of keys found in box i.
# containedBoxes[i]: list of boxes contained inside box i.
# initialBoxes: list of boxes you initially have.

# Your goal is to collect as many candies as possible.

# Hint:
# Use a queue to simulate the box-opening process.
# Only open boxes that are accessible and can be opened (have key or are open).
# Add new keys and new boxes found, repeat the process.
# Track visited boxes to prevent double counting.

from collections import deque

def maxCandies(status, candies, keys, containedBoxes, initialBoxes):
    n = len(status)
    visited = [False] * n
    has_key = status[:]  # current keys in hand (status 1 means openable)
    
    queue = deque()
    for box in initialBoxes:
        queue.append(box)
    
    total_candies = 0

    while queue:
        size = len(queue)
        progress = False  # to avoid infinite loops if no box can be opened
        for _ in range(size):
            box = queue.popleft()
            if visited[box] or not has_key[box]:
                queue.append(box)  # maybe we'll get the key later
                continue
            
            visited[box] = True
            total_candies += candies[box]
            progress = True

            # Add keys found inside this box
            for k in keys[box]:
                has_key[k] = 1

            # Add contained boxes
            for b in containedBoxes[box]:
                queue.append(b)
        
        # If no progress is made and queue has only unopened boxes, break to avoid infinite loop
        if not progress:
            break

    return total_candies


#Time and Space Complexity:
#Time: O(N + total keys + total containedBoxes)
#Space: O(N) for visited, has_key, and queue