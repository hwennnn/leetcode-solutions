class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter, visited, stack = collections.Counter(s), set(), []
        
        for c in s:
            counter[c] -= 1
            if c in visited: continue
            
            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                visited.remove(stack.pop())
            
            visited.add(c)
            stack.append(c)
        
        return "".join(stack)