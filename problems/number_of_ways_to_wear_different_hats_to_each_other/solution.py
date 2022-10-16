class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        n, maxN = len(hats), 41
        completed_mask = (1 << n) - 1
        s = collections.defaultdict(list)
        
        for i, hatList in enumerate(hats):
            for hat in hatList:
                s[hat].append(i)
        
        @cache
        def dfs(hat, mask):
            if mask == completed_mask: return 1
            if hat >= maxN: return 0
            
            res = dfs(hat + 1, mask) # skip current round
            
            for index in s[hat]:
                if mask & (1 << index): continue
                
                res = (res + dfs(hat + 1, mask | (1 << index))) % M
                
            return res
        
        return dfs(0, 0)
            
                
                
        