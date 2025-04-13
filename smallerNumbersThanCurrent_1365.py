
    def smallerNumbersThanCurrent(nums):

        temp = sorted((nums))
        d = {}
        for i, n in enumerate(temp):

            if n not in d:
                d[n] = i

        ret = []
        for i in  nums:
            ret.append(d[i])
        return ret



nums =[1,8,3,7,0,5]
print(smallerNumbersThanCurrent(nums))