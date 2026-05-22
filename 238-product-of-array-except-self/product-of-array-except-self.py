class Solution(object):
    def productExceptSelf(self, nums):
        product = 1
        productWithOutZero = 1
        haveZero = 0
        for i in nums:
            if i == 0:
                haveZero += 1
                product = 0
            else:
                product = product * i
                productWithOutZero = productWithOutZero * i
        if haveZero > 0:
            if ((haveZero == len(nums)-1) and (len(nums) == 2)):
                temp = nums[0]
                nums[0] = nums[1]
                nums[1] = temp
                return nums
            if  haveZero>1:
                for i in range(len(nums)):
                    nums[i] = 0
                return nums
            if haveZero == 1:
                for i in range(len(nums)):
                    if nums[i] == 0:
                        nums[i] = productWithOutZero
                    else:
                        nums[i] = 0
                return nums
        else:
            for i in range(len(nums)):
                nums[i] = product/nums[i]
        return nums

        