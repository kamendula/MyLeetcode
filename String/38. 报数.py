class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        import itertools
        def read(n):
            s = ""
            for k, v in itertools.groupby(str(n)):
                s += str(len(list(v))) + k
            print s
            return s

        cnt = 0
        out = "1"
        for i in range(1, n):
            out = read(out)
        return out
