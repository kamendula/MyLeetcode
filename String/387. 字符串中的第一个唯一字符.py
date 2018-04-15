class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        for c in s:
            if c not in m:
                m[c] = 0
            else:
                m[c] =1
        for i in xrange(len(s)):
            if m[s[i]] == 0:
                return i
        return -1