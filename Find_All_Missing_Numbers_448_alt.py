
nums = [2,4,5,6,7,4,2]
def find_missing(nums):
   for i in range(len(nums)):
       temp = abs(nums[i])-1
       if nums[temp] > 0:
           nums[temp] *= -1
   res = []
   for i,n in  enumerate(nums):
        if n > 0:
         res.append( i+1)
   return res
print(find_missing(nums))