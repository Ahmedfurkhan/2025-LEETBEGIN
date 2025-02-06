class Solution:
  def tupleSameProduct(self, nums: List[int]) -> int:
    n, result = len(nums), 0
    product_freq = {}

    for i in range(n):
      for j in range(i+1, n):  
        product = nums[i] * nums[j]
        if product in product_freq:
          result += 8 * product_freq[product]
          product_freq[product] += 1
        else:
          product_freq[product] = 1

    return result
        