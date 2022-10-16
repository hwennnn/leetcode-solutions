class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        res = float('inf')
        A = [0] * k
        
        def go(index):
            nonlocal res, A
            
            if index == n:
                res = min(res, max(A))
                return
            
            seen = set()
            
            for j in range(k):
                if A[j] in seen: continue
                if A[j] + jobs[index] >= res: continue
                
                seen.add(A[j])
                A[j] += jobs[index]
                go(index + 1)
                A[j] -= jobs[index]
        
        go(0)
        
        return res