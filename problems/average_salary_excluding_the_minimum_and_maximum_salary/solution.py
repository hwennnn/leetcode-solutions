class Solution:
    def average(self, salary: List[int]) -> float:
        mmax, mmin = max(salary), min(salary)
        res = count = 0
        
        for x in salary:
            if x != mmax and x != mmin:
                res += x
                count += 1
        
        return res / count