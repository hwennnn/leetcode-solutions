class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        nums = collections.Counter(s).values()
        odds = sum(i & 1 for i in nums)
        return len(s) - odds + bool(odds)