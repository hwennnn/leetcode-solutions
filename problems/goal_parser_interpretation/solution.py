class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        
        for x in command:
            stack.append(x)
            
            if len(stack) >= 2 and stack[-2] + stack[-1] == "()":
                stack.pop()
                stack.pop()
                stack.append("o")
            elif len(stack) >= 4 and "".join(stack[-4:]) == "(al)":
                for _ in range(4):
                    stack.pop()
                stack.append("al")
        
        return "".join(stack)