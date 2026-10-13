"""
Pattern: Backtracking
Problem: Subsets (LeetCode #78)
Description: Given an integer array nums of unique elements, return all 
possible subsets (the power set). The solution set must not contain duplicate subsets.
"""

def subsets(nums: list[int]) -> list[list[int]]:
    result = []
    
    def backtrack(start: int, current_subset: list[int]):
        result.append(list(current_subset))
        
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()
            
    backtrack(0, [])
    return result

# --- Test Cases ---
if __name__ == "__main__":
    nums = [1, 2, 3]
    print(f"Input: {nums}")
    print(f"All Subsets: {subsets(nums)}")
    print(f"Expected: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]")