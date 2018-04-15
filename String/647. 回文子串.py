class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def helper(i, j):
            res1 = 0
            while (i >= 0 and j < len(s) and s[i] == s[j]):
                res1 += 1
                i -= 1
                j += 1
            return res1

        res = 0
        for i, ss in enumerate(s):
            res += helper(i, i)

            res += helper(i, i + 1)

        return res