class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total = sum(chalk)
        k %= total
        
        for i, x in enumerate(chalk):
            if k < x: return i
            k -= x