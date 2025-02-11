from typing import List
from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = (n*(n-1)) // 2
        good_pairs = 0
        freq = defaultdict(int)
        for i in range(n):
            key = nums[i] - i
            good_pairs += freq[key]
            freq[key] += 1
        return total_pairs - good_pairs