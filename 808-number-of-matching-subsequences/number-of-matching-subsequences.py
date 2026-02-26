import bisect

class Solution(object):
    def numMatchingSubseq(self, s, words):
        dic_words = {}
        
        for i, ch in enumerate(s):
            dic_words.setdefault(ch, []).append(i)

        def helper(w):
            cur = -1
            for ch in w:
                if ch not in dic_words:
                    return False
                idx_list = dic_words[ch]
                pos = bisect.bisect_right(idx_list, cur)
                if pos == len(idx_list):
                    return False
                cur = idx_list[pos]
            return True

        return sum(helper(w) for w in words)