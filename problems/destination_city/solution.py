class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        mp = collections.defaultdict(int)
        
        for a, b in paths:
            mp[a] += 1
            mp[b] += 1
        
        for a,b in paths:
            if mp[b] == 1:
                return b