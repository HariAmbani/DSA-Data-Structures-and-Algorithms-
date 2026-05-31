class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()

        for i in asteroids:
            if i > mass:
                return False
            else:
                mass += i
        
        return True
        