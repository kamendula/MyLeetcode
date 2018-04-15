class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = {}
        for tt in set(t):
            m[tt] = t.count(tt)

        left = 0
        count = 0
        minlen = len(s) + 1
        r = ""
        for i in range(len(s)):
            if s[i] in m:
                m[s[i]] -= 1
                if m[s[i]] >= 0:
                    count += 1
            while (count == len(t)):
                if i - left + 1 < minlen:
                    minlen = i - left + 1
                    r = s[left:i + 1]
                if s[left] in m:
                    m[s[left]] += 1
                    if m[s[left]] > 0:
                        count -= 1

                left += 1
        return r