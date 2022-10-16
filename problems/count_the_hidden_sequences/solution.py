class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mmax = mmin = s = 0
        
        for x in differences:
            s += x
            
            mmax = max(mmax, s)
            mmin = min(mmin, s)
        
        res = 0
        
        for x in range(lower, upper + 1):
            if x + mmin >= lower and x + mmax <= upper:
                res += 1
        
        return res