from typing import List
from collections import Counter

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2  # Compute total possible pairs
        c = Counter(i - num for i, num in enumerate(nums))  # Count occurrences of nums[i] - i
        
        good_pairs = sum(v * (v - 1) // 2 for v in c.values())  # Sum of good pairs formula

        return total_pairs - good_pairs  # Bad pairs = total - good
