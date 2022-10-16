class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        deq, seen, res = deque([s]), {s}, s
        
        while deq:
            c = deq.popleft()
            res = min(res, c)
            A = list(c)
            
            for i in range(1,n,2):
                A[i] = str(((int(A[i])+a)%10))
            
            A = "".join(A)
            if A not in seen:
                seen.add(A)
                deq.append(A)
            
            rotate = c[b:] + c[:b]
            if rotate not in seen:
                seen.add(rotate)
                deq.append(rotate)
        
        return res
                