class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        N = len(nums)
        INF = inf
        
        @cache
        def go(index):
            if index == N: return 0
            
            res = INF
            mp = Counter()
            count = 0
            
            for j in range(index, N):
                mp[nums[j]] += 1
                
                if mp[nums[j]] > 2:
                    count += 1
                elif mp[nums[j]] == 2:
                    count += 2
                
                ans = k + count + go(j + 1)
                if ans < res:
                    res = ans
            
            return res
        
        return go(0)