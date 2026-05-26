class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        start = 0
        end = len(nums)-1

        while start<=end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid] :
                if target > nums[mid] or target < nums[start]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                if target < nums[mid] or target > nums[end]:
                    end = mid-1
                else:
                    start = mid+1
        return -1
        

        