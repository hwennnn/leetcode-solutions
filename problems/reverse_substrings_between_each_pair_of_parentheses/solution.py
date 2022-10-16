class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c == "(":
                stack.append([])
            elif c == ")":
                words = stack.pop()[::-1]
                if stack:
                    stack[-1] += words
                else:
                    stack.append(words)
            else:
                if stack:
                    stack[-1].append(c)
                else:
                    stack.append([c])
        
        return "".join(stack[-1])