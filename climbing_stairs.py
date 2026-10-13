"""
Pattern: Dynamic Programming
Problem: Climbing Stairs (LeetCode #70)
Description: You are climbing a staircase. It takes n steps to reach the top. 
Each time you can either climb 1 or 2 steps. Return the number of distinct ways you can climb to the top.
"""

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
        
    prev1 = 2  # ways to reach (i-1)
    prev2 = 1  # ways to reach (i-2)
    current = 0
    
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        
    return current

# --- Test Cases ---
if __name__ == "__main__":
    n = 5
    print(f"Input: n = {n}")
    print(f"Distinct Ways: {climb_stairs(n)} (Expected: 8)")