class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counter = Counter(s)
        
        for x in t:
            if counter[x] <= 0:
                return False
            
            counter[x] -= 1
        
        return True