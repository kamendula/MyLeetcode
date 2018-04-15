class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        res = strs[0]
        for s in strs[1:]:
            while s.find(res) != 0:
                res = res[:-1]
        return res