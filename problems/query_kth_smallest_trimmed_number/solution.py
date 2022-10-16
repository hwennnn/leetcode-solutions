class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        
        for k, trim in queries:
            A = []
            
            for i, x in enumerate(nums):
                A.append((x[-trim:], i))
            
            A.sort()
            
            res.append(A[k - 1][1])
        
        return res
            
            