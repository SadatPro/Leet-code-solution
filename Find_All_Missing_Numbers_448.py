
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        set_num = set(nums)
        
        ret = []

        for i in range(1,len(nums)+1):

            if i not in set_num:
                 ret.append(i)

        return ret           