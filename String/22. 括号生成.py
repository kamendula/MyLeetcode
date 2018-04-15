class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        s = ""
        self.addpair(res, s, n, 0)
        return res

    def addpair(self, res, s, left, right):
        if left == 0 and right == 0:
            res.append(s)
            return
        if right > 0:
            self.addpair(res, s + ")", left, right - 1)
        if left > 0:
            self.addpair(res, s + "(", left - 1, right + 1)
