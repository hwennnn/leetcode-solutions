class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = collections.Counter(s)
        values = list(counter.values())
        
        for v in values:
            if v != values[0]: return False
        
        return True