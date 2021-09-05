class Solution:
    def numberOfWeakCharacters(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x:(x[0], -x[1]))
        stack = []
        res = 0
        
        for a,b in A:
            while stack and a > stack[-1][0] and b > stack[-1][1]:
                stack.pop()
                res += 1
            
            stack.append((a, b))
        
        return res