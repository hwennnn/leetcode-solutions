class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0] * N
        stack = []

        for i, x in enumerate(temperatures):
            while stack and x > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            
            stack.append(i)
        
        return res