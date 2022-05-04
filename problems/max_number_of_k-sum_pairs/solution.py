class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        A = Counter(sorted(nums))
        res = 0
        
        for x in A.keys():
            if x > k: break
            
            target = k - x
            
            if target in A:
                res += min(A[x], A[target])
            
        return res // 2