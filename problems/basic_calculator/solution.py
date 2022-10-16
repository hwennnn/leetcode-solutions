class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        result = number = 0
        
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c == '+':
                result += sign * number
                number = 0
                sign = 1
            elif c == '-':
                result += sign * number
                number = 0
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                
                result = 0
                sign = 1
            elif c == ')':
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()
        
        if number != 0: 
            result += sign * number
        
        return result