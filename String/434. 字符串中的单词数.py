class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = s.split(" ")
        ans = 0
        for ee in ss:
            if ee != "":
                ans += 1
        return ans
