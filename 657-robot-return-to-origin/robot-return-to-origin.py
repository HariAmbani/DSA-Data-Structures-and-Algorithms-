class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vertical = 0
        horizontal = 0

        for i in moves:
            if i == 'U':
                vertical += 1
            elif i == 'D':
                vertical -= 1
            elif i == "L":
                horizontal += 1
            elif i == "R":
                horizontal -= 1
        
        if ((vertical == 0) and (horizontal == 0)):
            return True
        else:
            return False