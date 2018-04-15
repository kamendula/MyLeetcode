class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        s_dict = {}
        for i, s in enumerate(S):
            s_dict[s] = i
        def r_value(x):
            if x in s_dict:
                return s_dict[x]
            else:
                return 27
        t = sorted(T, key = lambda x : r_value(x))
        return "".join(t)