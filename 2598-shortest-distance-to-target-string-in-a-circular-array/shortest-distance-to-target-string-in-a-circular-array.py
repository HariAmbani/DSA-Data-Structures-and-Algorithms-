class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        word = {}
        for i in range(len(words)):
            if words[i] in word:
                word[words[i]].append(i)
            else:
                word[words[i]] = [i]
        
        mini = float('inf')
        if target in word:
            for j in word[target]:
                mini = min(mini, (j-startIndex)%len(words), (startIndex-j)%len(words))
            return mini
        else:
            return -1
        