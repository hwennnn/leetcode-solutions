class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        
        for x in nums:
            curr = []
            
            while x > 0:
                curr.append(x % 10)
                x //= 10
            
            res += curr[::-1]
        
        return res