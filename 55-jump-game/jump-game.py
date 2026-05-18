class Solution(object):
    def canJump(self, nums):
        distance = 1
        can_reach = True
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i] >= distance:
                can_reach = True
                distance = 1
            else:
                can_reach = False
                distance += 1
    
        return can_reach
        


        