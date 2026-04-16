class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = float('inf')

        num_dict = {}
        for i in range(len(nums)):
            if nums[i] in num_dict:
                num_dict[nums[i]].append(i)
            else:
                num_dict[nums[i]]=[i]
        
        for j in num_dict.values():
            if len(j) > 2:
                for k in range(len(j)-2):
                    maxi = min(maxi, (j[k+1]-j[k])+(j[k+2]-j[k+1])+(j[k+2]-j[k]))
        
        if maxi == float('inf'):
            return -1
        else:
            return maxi


        