class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        
        res = [0] * len(arr)
        stack = []
        
        for i,x in enumerate(arr):
            
            while stack and x > arr[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            
            stack.append(i)
        
        return res