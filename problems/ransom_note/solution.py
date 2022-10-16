class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = collections.Counter(ransomNote)
        n = len(mp)
        
        for word in magazine:
            mp[word] -= 1
            if mp[word] == 0:
                n -= 1
            
            if n == 0: return True
        
        return False