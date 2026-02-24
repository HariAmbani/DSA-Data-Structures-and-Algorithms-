class Solution(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            fibo_two = 2

        fibo_one = 1
        fibo_two = 2

        for i in range(2, n+1):
            temp = fibo_two
            fibo_two = fibo_one + fibo_two
            fibo_one = temp
        
        ans = pow(fibo_two, 2)%(pow(10, 9)+7)

        return ans
    
        

        