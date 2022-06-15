class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        mp = defaultdict(set)
        n, m = len(s), len(sub)

        for a, b in mappings:
            mp[b].add(a)
            
        for i in range(n):
            if i + m > n: return False
            
            for j in range(m):
                if not (sub[j] == s[i + j] or sub[j] in mp[s[i + j]]):
                    break
                
                if j == m - 1:
                    return True
        
        return False