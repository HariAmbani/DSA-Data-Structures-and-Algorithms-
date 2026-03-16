class TimeMap(object):

    def __init__(self):
        self.timemap_dict = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.timemap_dict:
            self.timemap_dict[key].append([timestamp, value])
        else:
            self.timemap_dict[key]= [[timestamp, value]]
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.timemap_dict:
            return ""
        
        arr = self.timemap_dict[key]
        start = 0
        end = len(arr)-1

        ans = ""
        while start <= end:
            mid = (start+end)//2

            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                start = mid + 1
            
            else:
                end = mid - 1
        
        return ans

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)