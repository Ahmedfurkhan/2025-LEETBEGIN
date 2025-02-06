class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)
    
        # Step 1: Generate all possible products
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1
        
        # Step 2: Count valid tuples
        result = 0
        for count in product_count.values():
            if count >= 2:
                result += count * (count - 1) // 2 * 8
        
        return result