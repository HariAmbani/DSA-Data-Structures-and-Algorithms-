class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        if n < 3:
            return True

        start = nums[0]
        found = 0
        
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                if found > 0:
                    print("1")
                    return False
                elif nums[i] <= nums[0]:
                    print("2")
                    found += 1
                else:
                    print("3")
                    return False
        
        if ((found == 0) or (found == 1 and nums[0] >= nums[-1])):
            print("4")
            return True
        else:
            print("5")
            return False 
        