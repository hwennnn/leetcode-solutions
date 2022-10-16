class Solution:
    def robotWithString(self, s: str) -> str:
        N = len(s)
        res = []
        stack = []
        count = Counter(s)
        
        for x in s:
            stack.append(x)
            
            if count[x] == 1:
                del count[x]
            else:
                count[x] -= 1
            
            while stack and count and stack[-1] <= min(count):
                res.append(stack.pop())
        
        if stack:
            res += stack[::-1]
        
        return "".join(res)