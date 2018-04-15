class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dict = {}
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s not in str_dict:
                str_dict[sort_s] = []
            str_dict[sort_s].append(s)
        return str_dict.values()