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
            if i == 'D':
                vertical -= 1
            if i == "L":
                horizontal += 1
            if i == "R":
                horizontal -= 1
        
        if ((vertical == 0) and (horizontal == 0)):
            return True
        else:
            return False