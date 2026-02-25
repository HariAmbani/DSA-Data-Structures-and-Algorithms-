class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)

        # If total is odd → cannot partition
        if total % 2 != 0:
            return False
        
        target = total // 2

        all_posi = set()
        all_posi.add(0)

        for i in nums:
            cur = set(all_posi)
            for j in all_posi:
                if i + j == target:
                    return True
                elif i + j < target:
                    cur.add(i+j)
            all_posi = cur
        return False


        
        
        
            

        
