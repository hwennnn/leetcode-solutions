class Solution:
    def slowestKey(self, rt: List[int], kp: str) -> str:

        m = float('-inf')
        res = ""
        prev = 0
        for i,t in enumerate(rt):
            v = t - prev

            if v >= m:
                m = v
                res = kp[i]
            
            prev = t

        return res
            