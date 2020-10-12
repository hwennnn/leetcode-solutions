class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        res = [0] * len(T)
        
        stack = []
        
        for i, x in enumerate(T):
            
            while stack and T[stack[-1]] < x:
                tmp = stack.pop()
                res[tmp] = i - tmp
            
            stack.append(i)
        
        return res