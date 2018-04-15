class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        return self.helper(t)

    def helper(self, t):
        if t == None:
            return "";
        s = str(t.val)
        s1 = self.helper(t.left)
        s2 = self.helper(t.right)
        if s1 != "" and s2 != "":
            s += "(" + s1 + ")" + "(" + s2 + ")"
        elif s1 != "":
            s += "(" + s1 + ")"
        elif s2 != "":
            s += "()(" + s2 + ")"
        return s
