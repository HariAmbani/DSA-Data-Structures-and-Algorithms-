class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        odd_dict_s1 = {}
        even_dict_s1 = {}

        odd_dict_s2 = {}
        even_dict_s2 = {}

        for i in range(len(s1)):

            if i % 2 == 0:
                if s1[i] in even_dict_s1:
                    even_dict_s1[s1[i]] += 1
                else:
                    even_dict_s1[s1[i]] = 1

                if s2[i] in even_dict_s2:
                    even_dict_s2[s2[i]] += 1
                else:
                    even_dict_s2[s2[i]] = 1

            else:
                if s1[i] in odd_dict_s1:
                    odd_dict_s1[s1[i]] += 1
                else:
                    odd_dict_s1[s1[i]] = 1

                if s2[i] in odd_dict_s2:
                    odd_dict_s2[s2[i]] += 1
                else:
                    odd_dict_s2[s2[i]] = 1

        if ((odd_dict_s1 == odd_dict_s2) and (even_dict_s1 == even_dict_s2)):
            return True
        else:
            return False
        