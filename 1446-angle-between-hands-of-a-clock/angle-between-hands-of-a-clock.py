class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour_angle = ((hour%12) * 30) + float(minutes)/2
        print(hour_angle)

        minutes_angle = minutes * 6
        print(minutes_angle)

        dif = abs(hour_angle - minutes_angle)

        if dif > 180:
            return 360 - dif
        else:
            return dif


        