"""
Pattern: Breadth-First Search (BFS) / Trees
Problem: Binary Tree Level Order Traversal (LeetCode #102)
Description: Given the root of a binary tree, return the level order 
traversal of its nodes' values (i.e., from left to right, level by level).
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
        
    return result

# --- Test Cases ---
if __name__ == "__main__":
    # Constructing a simple tree: [3, 9, 20, null, null, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    print(f"Level Order Traversal: {level_order(root)}")
    print(f"Expected: [[3], [9, 20], [15, 7]]")