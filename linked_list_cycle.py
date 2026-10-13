"""
Pattern: Fast & Slow Pointers
Problem: Linked List Cycle (LeetCode #141)
Description: Given head, the head of a linked list, determine if there 
is a cycle in the linked list.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          # Moves 1 step
        fast = fast.next.next     # Moves 2 steps
        
        if slow == fast:
            return True           # Cycle detected
            
    return False                  # No cycle

# --- Test Cases ---
if __name__ == "__main__":
    # Creating a cycle for testing: 3 -> 2 -> 0 -> 4 -> (points back to 2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 # Cycle here
    
    print(f"Cycle Detected: {has_cycle(node1)} (Expected: True)")