class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        res = []
        potions.sort()
        
        for spell in spells:
            index = bisect_left(potions, (success + spell - 1) // spell)
            res.append(n - index)
        
        return res
        
        