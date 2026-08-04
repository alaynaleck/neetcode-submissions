class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixProducts = [0] * len(nums)
        suffixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            suffixProducts[i] = suffixProduct
            suffixProduct = suffixProduct * nums[i]
            
        products = []
        prefixProduct = 1
        for i in range(len(nums)):
            products.append(suffixProducts[i] * prefixProduct)
            prefixProduct = prefixProduct * nums[i]

        return products