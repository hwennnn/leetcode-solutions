class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        
        for num in nums:
            s = set()
            for i in range(1, floor(sqrt(num)) + 1):
                
                if num % i == 0:
                    s.add(num//i)
                    s.add(i)
                
                if len(s) > 4:
                    break
            
            if len(s) == 4:
                res += sum(s)
        
        return res