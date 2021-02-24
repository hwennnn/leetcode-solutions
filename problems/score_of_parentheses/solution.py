class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        curr = 0
        
        for c in S:
            if c == "(":
                stack.append(curr)
                curr = 0
            else:
                curr = stack.pop() + max(curr*2, 1)
        
        return curr