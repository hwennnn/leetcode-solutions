class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        
        def construct(A):
            s = set()
            
            for k in range(len(A) + 1):
                for comb in combinations(A, k):
                    s.add(sum(comb))
            
            return s
        
        n = len(nums) // 2
        s1, s2 = construct(nums[:n]), construct(nums[n:])
        s2 = sorted(s2)
        res = float('inf')
        
        for x in s1:
            target = goal - x
            index = bisect.bisect_left(s2, target)
            
            for p in (index, index - 1):
                if 0 <= p < len(s2):
                    res = min(res, abs(x + s2[p] - goal))
        
        return res