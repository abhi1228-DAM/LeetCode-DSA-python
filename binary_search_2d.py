"""
2D Matrix Binary Search Implementation
Time Complexity: O(log(m * n))
Space Complexity: O(1)
"""

def binary_search_2d(matrix: list[list[int]], target: int) -> bool:
    """
    Searches for a target value in an m x n integer matrix with the following properties:
    1. Each row is sorted in non-decreasing order.
    2. The first integer of each row is greater than the last integer of the previous row.
    """
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    
    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        # Convert 1D virtual index 'mid' into 2D row and column indices
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


if __name__ == "__main__":
    # Test Case 1: Standard 2D Matrix
    grid = [
        [1,  3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]

    print("--- 2D Binary Search Tests ---")
    print(f"Search for 3  (Expected: True):  {binary_search_2d(grid, 3)}")
    print(f"Search for 16 (Expected: True):  {binary_search_2d(grid, 16)}")
    print(f"Search for 13 (Expected: False): {binary_search_2d(grid, 13)}")
    print(f"Search for 60 (Expected: True):  {binary_search_2d(grid, 60)}")