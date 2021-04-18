class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for c in s:
            if stack and stack[-1][0] == c:
                ch, cnt = stack.pop()
                stack.append((ch, cnt + 1))
            else:
                stack.append((c, 1))
            
            if stack and stack[-1][1] == k:
                stack.pop()
        
        return "".join(ch * cnt for ch, cnt in stack)