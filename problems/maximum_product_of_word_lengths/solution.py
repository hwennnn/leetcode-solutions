class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        mp = collections.defaultdict(int)
        
        for word in words:
            mask = 0
            
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            
            mp[mask] = max(mp[mask], len(word))
        
        return max([mp[mask1] * mp[mask2] for mask1 in mp for mask2 in mp if mask1 & mask2 == 0] or [0])