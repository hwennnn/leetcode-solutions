class Solution:
    def findRepeatedDnaSequences(self, S: str) -> List[str]:
        n = len(S)
        if n <= 10: return []
        
        mp = collections.defaultdict(int)
        
        res = []
        for i in range(n-9):
            key = S[i:i+10]
            mp[key] += 1
            if mp[key] == 2:
                res.append(key)
        
        return res