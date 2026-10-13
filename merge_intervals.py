"""
Pattern: Intervals / Greedy
Problem: Merge Intervals (LeetCode #56)
Description: Given an array of intervals where intervals[i] = [start_i, end_i], 
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input.
"""

def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
        
    # Sort intervals based on the starting value
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        # If current interval overlaps with the last merged one, merge them
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
            
    return merged

# --- Test Cases ---
if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Input Intervals: {intervals}")
    print(f"Merged Intervals: {merge(intervals)} (Expected: [[1, 6], [8, 10], [15, 18]])")