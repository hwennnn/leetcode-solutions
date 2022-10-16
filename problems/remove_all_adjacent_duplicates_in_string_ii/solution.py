class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for x in s:
            if stack and stack[-1][0] == x:
                _, cnt = stack.pop()
                stack.append((x, cnt + 1))
            else:
                stack.append((x, 1))
            
            if stack and stack[-1][1] == k:
                stack.pop()
            
        return "".join(x * cnt for x, cnt in stack)