class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi1 = float('-inf')
        maxi2 = float('-inf')
        maxi3 = float('-inf')

        for i in nums:
            if i > maxi1:
                print('1')
                maxi3 = maxi2
                maxi2 = maxi1
                maxi1 = i
            elif i > maxi2 and i != maxi1:
                print('2')
                maxi3 = maxi2
                maxi2 = i
            elif i > maxi3 and i not in [maxi1, maxi2]:
                print('3')
                maxi3 = i

        print("-------------")
        print(maxi1)
        print(maxi2)
        print(maxi3)

        return maxi3 if maxi3 != float('-inf') else maxi1
        