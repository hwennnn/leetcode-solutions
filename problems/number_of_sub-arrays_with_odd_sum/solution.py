class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        odd = even = res = 0
        M = 1000000007
        
        for num in arr:
            if num & 1:
                odd, even = even+1, odd
            else:
                odd, even = odd, even+1
                
            res += odd
        
        return res%M
        