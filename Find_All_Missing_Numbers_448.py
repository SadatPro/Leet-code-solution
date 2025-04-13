
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        set_num = set(nums)
        
        ret = []

        for i in range(1,len(nums)+1):

            if i not in set_num:
                 ret.append(i)

        return ret

nums = [4,3,2,7,8,2,3,1]
sol = Solution()
result = sol.findDisappearedNumbers(nums)
print(result)  # এই লাইনটা না থাকলে কিছুই দেখাবে না
