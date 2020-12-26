class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        k = 3
        res = sum(arr)
        
        while k <= n:
            for i in range(n-k+1):
                res += sum(arr[i:i+k])
            
            k += 2
        
        return res