
nums = [1,3,4,0]

def find_missing(nums):
    #sum(range(len(nums) + 1)) এই ধারার সংখ্যা যোগ করে। আমাদের উদাহরণে sum([0, 1, 2, 3]) = 6
    return sum(range(len(nums)+1)) - sum(nums)