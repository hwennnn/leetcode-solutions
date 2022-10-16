class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        
        child = cook = 0
        
        while child<len(g) and cook<len(s):
            
            child += s[cook] >= g[child]
            cook += 1
        
        return child