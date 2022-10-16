class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = int(left)
        right = int(right)
        
        res = [1,2,3,4,5,6,7,8,9]
        
        for i in range(1, 10000):
            s = int(str(i) + str(i)[::-1])
            res.append(s)
            
            for j in range(10):
                res.append(int(str(i) + str(j) + str(i)[::-1]))

        def isPalindrome(s):
            return s == s[::-1]
        
        count = 0
        
        for val in res:
            s = val * val
            
            if left <= s <= right and isPalindrome(str(s)):
                count += 1
        
        return count