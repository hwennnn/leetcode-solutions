class Solution:
    def peopleIndexes(self, fc: List[List[str]]) -> List[int]:
        ans = []
        
        s = [set(cs) for cs in fc]
        
        res = []
        
        for i,s1 in enumerate(s):
            
            if all(i == j or not s1.issubset(s2) for j,s2 in enumerate(s)):
                res.append(i)
        
        return res