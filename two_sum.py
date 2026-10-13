"""
Pattern: Two Pointers / Hash Map
Problem: Two Sum (LeetCode #1)
Description: Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# --- Test Cases ---
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Input: {nums}, Target: {target}")
    print(f"Output Indices: {two_sum(nums, target)} (Expected: [0, 1])")