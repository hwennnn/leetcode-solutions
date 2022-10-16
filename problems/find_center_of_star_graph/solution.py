class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        mp = collections.defaultdict(int)
        
        for a,b in edges:
            mp[a] += 1
            mp[b] += 1
        
        for key in mp:
            if mp[key] == n:
                return key
        
        return -1
        