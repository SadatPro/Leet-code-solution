class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
         if len(set(nums)) == len(nums):
            return False
         else:
            return True
    
nums = [1,2,3,3]

sol = Solution()
result = sol.containsDuplicate(nums)
print(result)  # এই লাইনটা না থাকলে কিছুই দেখাবে না
