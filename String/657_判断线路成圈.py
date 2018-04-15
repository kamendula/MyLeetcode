class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for m in moves:
            if m == "L":
                y -= 1
            elif m == "R":
                y += 1
            elif m == "U":
                x += 1
            else:
                x -= 1
        return x == y == 0