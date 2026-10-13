"""
Pattern: Sliding Window
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Description: Given a string s, find the length of the longest substring 
without repeating characters.
"""

def length_of_longest_substring(s: str) -> int:
    char_map = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        char_map[s[right]] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len

# --- Test Cases ---
if __name__ == "__main__":
    test_str = "abcabcbb"
    print(f"Input: '{test_str}'")
    print(f"Longest Substring Length: {length_of_longest_substring(test_str)} (Expected: 3)")