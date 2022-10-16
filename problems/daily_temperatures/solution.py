class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        stack = []
        res = [0] * n
        
        for i, x in enumerate(T):
            while stack and x > T[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            
            stack.append(i)
        
        return res
        
        