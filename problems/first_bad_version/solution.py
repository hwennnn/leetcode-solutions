# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        
        while left < right:
            mid = (left+right)//2
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return left