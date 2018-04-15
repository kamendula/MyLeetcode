class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = [1]
        for i in xrange(1, len(s)):
            if s[i] != s[i-1]:
                groups.append(1)
            else:
                groups[-1] += 1
        ans = 0
        for i in xrange(0,len(groups)-1):
            ans += min(groups[i], groups[i+1])
        return ans