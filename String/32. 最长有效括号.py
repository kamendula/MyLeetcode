class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        res = 0
        start = 0
        for i, ss in enumerate(s):
            if ss == "(":
                l.append(i)
            else:
                if len(l) != 0:
                    l.pop()
                    if len(l) == 0:
                        res = max(res, i - start +1)  #+1 是因为 start位置是正好包含的那个位置。 而下一个不加1是因为l[-1]是不包含在里面的。
                    else:
                        res = max(res, i - l[-1])
                else:
                    start = i + 1
        return res