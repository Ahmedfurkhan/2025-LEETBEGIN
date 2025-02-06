class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        product_map = dict()

        res = 0

        for idx, num in enumerate(nums[:-1]):
            for numb in nums[idx + 1:]:
                product = num * numb

                if product in product_map:
                    product_map[product] += 1
                else:
                    product_map[product] = 1

        for k, v in product_map.items():
            if v > 1:
                res += (v*(v-1)//2) * (2**3)

        return res