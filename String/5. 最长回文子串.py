class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        maxlen = 0
        out = ""
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > maxlen:
                    maxlen = right - left + 1
                    out = s[left:right + 1]
                left -= 1
                right += 1

        for i in range(len(s)):
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > maxlen:
                    maxlen = right - left + 1
                    out = s[left:right + 1]
                left -= 1
                right += 1

        return out