class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        def check(num):
            num_str = str(num)
            for n in ["3", "4", "7"]:
                if num_str.find(n) != -1:
                    return 0

            set_str = set(num_str)
            for s in set_str:
                if s not in ["0", "1", "8"]:
                    return 1
            return 0

        ans = 0
        for i in range(1, N + 1):
            ans += check(i)
        return ans