class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """
    def concatenetedString(self, s1, s2):
        # write your code here
        new_s1 = ''
        new_s2 = ''

        for ch in s1:
            if ch not in s2:
                new_s1 += ch

        for ch in s2:
            if ch not in s1:
                new_s2 += ch

        return new_s1 + new_s2
