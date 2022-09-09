class Solution:
    def numberOfWeakCharacters(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x : (x[0], -x[1]))
        res = 0
        stack = []
        
        for a, b in A:
            while stack and a > stack[-1][0] and b > stack[-1][1]:
                res += 1
                stack.pop()
            
            stack.append((a, b))
        
        return res