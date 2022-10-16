class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], K: int) -> int:
        rows, cols = len(piles), len(piles[0])
        
        @cache
        def go(rowIndex, k):
            if k == 0: return 0
            if rowIndex == rows: return 0
            
            res = 0
            curr = 0
            currK = k
            
            # skip to take this
            res = max(res, go(rowIndex + 1, k))
            
            for i, x in enumerate(piles[rowIndex]):
                curr += x
                currK -= 1
                
                if currK >= 0:
                    res = max(res, curr + go(rowIndex + 1, currK))
                else:
                    break
            
            return res
        
        return go(0, K)