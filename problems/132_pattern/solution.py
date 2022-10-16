class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, mid = [], float("-inf")
        
        for num in nums[::-1]:
            if num < mid: return True
            else:
                while stack and num > stack[-1]:
                    mid = stack.pop()
            
            stack.append(num)
            
        return False