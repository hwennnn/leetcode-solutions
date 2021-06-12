class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        ssum = k % (sum(chalk))

        for i,x in enumerate(chalk):
            if ssum < x: return i
            
            ssum -= x
        
        