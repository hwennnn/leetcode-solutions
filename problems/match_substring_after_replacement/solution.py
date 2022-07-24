class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        mp = defaultdict(set)
        n, m = len(s), len(sub)
        
        for a, b in mappings:
            mp[b].add(a)
        
        def go(index, curr):
            if curr == m:
                return True
            
            if index == n:
                return False
            
            if sub[curr] == s[index] or sub[curr] in mp[s[index]]:
                return go(index + 1, curr + 1)
            
            return False
            
        for i, x in enumerate(s):
            if go(i, 0):
                return True
        
        return False