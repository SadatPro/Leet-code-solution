class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        sq_list = [num ** 2 for num in nums]
        sq_list.sort()
        return sq_list
