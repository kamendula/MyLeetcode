class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)/2):
            if len(s) % (i+1) == 0:
                new_s = s[0:i+1] *(len(s)/(i+1))
                if new_s == s:
                    return True
        return False