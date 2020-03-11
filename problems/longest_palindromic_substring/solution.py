class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)

        return res
       
        
    def helper(self,s,l,r):
        
        while 0<=l and r < len(s) and s[l]==s[r]:
                l-=1; r+=1
        return s[l+1:r]