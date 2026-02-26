class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        dic_words = {}

        for i in range(len(s)):
            if s[i] in dic_words:
                dic_words[s[i]].append(i)
            else:
                dic_words[s[i]] = [i]

        def find_next_greater_index_using_binary_search(i, start, cur):
            arr = dic_words[i]
            end = len(arr) - 1
            ans = -1

            while start <= end:
                mid = start + (end - start) // 2

                if arr[mid] > cur:
                    ans = mid
                    end = mid - 1
                else:
                    start = mid + 1

            return ans
        
        def helper(w):
            cur = -1
            dic_letter = {}
            for i in w:
                if i not in dic_words:
                    return False
                elif i not in dic_letter:
                    j = find_next_greater_index_using_binary_search(i, 0, cur)
                    if j == -1:
                        return False
                    else:
                        dic_letter[i] = j
                        cur = dic_words[i][j]
                else:
                    j =find_next_greater_index_using_binary_search(i, dic_letter[i]+1, cur)
                    if j == -1:
                        return False
                    else:
                        dic_letter[i]= j
                        cur = dic_words[i][j]
            return True

        ans = 0
        for j in words:
            if helper(j):
                ans += 1
        return ans               
        