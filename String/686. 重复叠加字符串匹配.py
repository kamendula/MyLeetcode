class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        new_a = ""
        cnt = 0
        while(len(new_a) < len(B)):
            new_a += A
            cnt += 1
        if new_a.find(B) != -1:
            return cnt
        new_a += A
        return cnt + 1 if new_a.find(B) != -1 else -1