"""
Pattern: Graph / Matrix Traversal (Breadth-First Search)
Problem: Number of Islands (LeetCode #200)
Description: Given an m x n 2D binary grid grid which represents a map of '1's (land) 
and '0's (water), return the number of islands.
"""

import collections

def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    visited = set()
    island_count = 0
    
    def bfs(r, c):
        queue = collections.deque([(r, c)])
        visited.add((r, c))
        
        while queue:
            row, col = queue.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 
                    0 <= nc < cols and 
                    grid[nr][nc] == "1" and 
                    (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                island_count += 1
                
    return island_count

# --- Test Cases ---
if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print("Input Grid:")
    for row in grid:
        print(row)
    print(f"Number of Islands: {num_islands(grid)} (Expected: 1)")