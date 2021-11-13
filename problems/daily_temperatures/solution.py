class Solution:
    def dailyTemperatures(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        stack = []
        
        for i, x in enumerate(A):
            while stack and x > A[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            
            stack.append(i)
        
        return res
            