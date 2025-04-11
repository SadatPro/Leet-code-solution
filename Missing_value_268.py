nums = [1,3,4,0]

nums.sort()
def find_missing(nums):
 for i,v in enumerate(nums):
    if (i != v):
         return v-1
     
    #এটি নিশ্চিত করে যে, যদি তালিকার কোনো মিসিং সংখ্যা না থাকে, তাহলে ধারার পরবর্তী সম্ভাব্য সংখ্যাটি রিটার্ন করা হবে।
    if(i == len(nums)-1):
        return v+1
    
print(find_missing(nums))


 