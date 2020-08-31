class Solution:
    def average(self, salary: List[int]) -> float:
        s_min = float('inf')
        s_max = float('-inf')
        n = len(salary)
        res = 0
        
        for s in salary:
            res += s
            s_min = min(s_min, s)
            s_max = max(s_max, s)

        return (res-s_min-s_max)/(n-2)