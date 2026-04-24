class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        l = moves.count("L")
        r = moves.count("R")
        u = moves.count("_")
        return (abs(l-r)+u) 

        # cur = 0
        # no_ = 0
        
        # for i in moves:
        #     if i == "_":
        #         no_ += 1
        #     elif i == "L":
        #         cur -= 1
        #     elif i == "R":
        #         cur += 1
        
        # if cur >= 0:
        #     return cur+no_
        # else:
        #     return abs(cur-no_)
        


        