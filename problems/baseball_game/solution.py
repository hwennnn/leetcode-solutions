class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for x in ops:
            if x == "C":
                stack.pop()
            elif x == "D":
                stack.append(stack[-1] * 2)
            elif x == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(x))
        
        return sum(stack)