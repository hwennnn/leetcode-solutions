class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(c))

        return stack.pop()