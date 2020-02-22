class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        return sum([sum1 != sum2 for sum1,sum2 in zip(heights,sorted(heights))])
        