"""
Pattern: Heaps / Priority Queues
Problem: Kth Largest Element in an Array (LeetCode #215)
Description: Given an integer array nums and an integer k, return the 
kth largest element in the array.
"""

import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    # Python's heapq is a min-heap by default. 
    # By keeping the heap size at k, the root will be the kth largest element.
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    return min_heap[0]

# --- Test Cases ---
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Kth Largest Element: {find_kth_largest(nums, k)} (Expected: 5)")