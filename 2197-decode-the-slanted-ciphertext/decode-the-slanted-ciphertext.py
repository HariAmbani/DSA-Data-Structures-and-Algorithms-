class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """

        if rows == 1:
            return encodedText

        ans = []
        total_count = len(encodedText)
        cols = total_count//rows

        for i in range(cols):
            j = i
            while (j < total_count):
                ans.append(encodedText[j])
                j += (cols+1)
        
        return (''.join(ans)).rstrip()
        