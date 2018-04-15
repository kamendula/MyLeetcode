class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = 0
        m = set()
        maxlen = 0
        for left in range(len(s)):
            right = left
            m.clear()
            while right < len(s):
                if s[right] not in m:
                    m.add(s[right])
                    right += 1
                else:
                    new_len = right - left
                    if new_len > maxlen:
                        maxlen = new_len
                    break
            if len(m) != 0:
                if maxlen < len(m):
                    maxlen = len(m)
        return maxlen