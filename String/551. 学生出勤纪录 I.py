class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') <= 1 and s.find("LLL") == -1:
            return True
        else:
            return False