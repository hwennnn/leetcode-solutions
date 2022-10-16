class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        scores = collections.defaultdict(int)
        n = len(nums)
        per = n // k
        candidates = []
        
        for mask in range(1 << n):
            count = 0
            
            for j in range(n):
                if mask & (1 << j) > 0:
                    count += 1
            
            if count == per:
                s = set()
                
                for j in range(n):
                    if mask & (1 << j) > 0: 
                        s.add(nums[j])
                
                if len(s) != per: continue
                
                candidates.append(mask) 
                scores[mask] = max(s) - min(s)
        
        @cache
        def go(mask):
            if mask == 0: return 0
            
            res = float('inf')
            
            for candidate in candidates:
                if (mask & candidate) == candidate:
                    res = min(res, go(mask ^ candidate) + scores[candidate])
            
            return res
        
        ans = go((1 << n) - 1)
        
        return -1 if ans == float('inf') else ans