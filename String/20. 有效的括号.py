class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_list = ['(', '[', '{']
        right_list = [')', ']', '}']
        to_cmp_left_list = []
        to_cmp_right_list = []
        n1 = 0
        n2 = 0
        n3 = 0
        for s0 in s:
            if s0 in left_list:
                to_cmp_left_list.append(s0)
            if s0 in right_list:
                if not to_cmp_left_list:
                    return False
                if left_list.index(to_cmp_left_list[-1]) != right_list.index(s0):
                    return False
                else:
                    to_cmp_left_list = to_cmp_left_list[:-1]
        if to_cmp_left_list:
            return False
        return True
