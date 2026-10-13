"""
Pattern: Two Pointers (Opposite Ends)
Problem: Container With Most Water (LeetCode #11)
Description: Given n non-negative integers representing an elevation map where 
the width of each bar is 1, find two lines that together with the x-axis form 
a container, such that the container contains the most water.
"""

def max_area(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate width and height of the container
        width = right - left
        current_height = min(height[left], height[right])
        current_water = width * current_height
        max_water = max(max_water, current_water)
        
        # Move the pointer of the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water

# --- Test Cases ---
if __name__ == "__main__":
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Input Heights: {heights}")
    print(f"Max Area: {max_area(heights)} (Expected: 49)")