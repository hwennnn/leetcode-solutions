class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        put = set()
        
        for x in s:
            counter[x] -= 1
            
            if x in put: continue
                
            while stack and x < stack[-1] and counter[stack[-1]] > 0:
                put.remove(stack.pop())
            
            stack.append(x)
            put.add(x)

        return "".join(stack)