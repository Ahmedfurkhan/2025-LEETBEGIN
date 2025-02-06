from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = dict()  # To store the frequency of each product
        res = 0  # To store the final result

        # Step 1: Generate all possible products of pairs (a, b)
        for idx, num in enumerate(nums[:-1]):
            for numb in nums[idx + 1:]:
                product = num * numb
                if product in product_map:
                    product_map[product] += 1
                else:
                    product_map[product] = 1

        # Step 2: Count valid tuples
        for v in product_map.values():
            if v > 1:
                res += (v * (v - 1) // 2) * 8  # Correct formula

        return res