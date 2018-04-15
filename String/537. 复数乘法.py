class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_items = a.split("+")
        b_items = b.split("+")
        if len(a_items) != 2 or len(b_items) !=2:
            return ""
        x1 = int(a_items[0])
        y1 = int(a_items[1][:-1])
        x2 = int(b_items[0])
        y2 = int(b_items[1][:-1])
        x_real = x1*x2 - y1*y2
        x_img = y1 * x2 + y2 * x1
        return str(x_real) + "+" + str(x_img) + "i"