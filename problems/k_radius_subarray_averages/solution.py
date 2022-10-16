class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        prefix = [0] + list(accumulate(nums))
        
        for i in range(k, n - k):
            x = (prefix[i + k + 1] - prefix[i - k]) // (k + k + 1)
            res[i] = x
        
        return res