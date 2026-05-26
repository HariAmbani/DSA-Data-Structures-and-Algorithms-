class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start,end = 0, len(nums)-1

        while start<=end:
            mid = (start+end)//2
            if target == nums[mid]:
                return mid
            elif nums[start] <= nums[mid]:
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