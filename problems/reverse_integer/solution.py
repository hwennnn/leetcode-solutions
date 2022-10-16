class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = cmp(x, 0) * int(str(abs(x))[::-1])
        return n if n.bit_length() < 32 else 0
