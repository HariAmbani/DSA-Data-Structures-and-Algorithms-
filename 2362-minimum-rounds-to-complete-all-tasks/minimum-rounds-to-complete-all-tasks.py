class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        task_count = {}

        for i in tasks:
            if i in task_count:
                task_count[i] += 1
            else:
                task_count[i] = 1

        ans = 0

        for i in task_count.values():
            if i == 1:
                return -1
            ans += i//3
            if i%3 != 0:
                ans += 1
        
        return ans
        