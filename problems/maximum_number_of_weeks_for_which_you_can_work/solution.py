class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        ssum, mmax = sum(milestones), max(milestones)
        
        if ssum - mmax >= mmax: return ssum
        
        return 2 * (ssum - mmax) + 1