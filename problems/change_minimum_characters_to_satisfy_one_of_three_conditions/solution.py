class Solution:
    def minCharacters(self, A: str, B: str) -> int:
        countA = Counter(ord(c) - ord('a') for c in A)
        countB = Counter(ord(c) - ord('a') for c in B)
    
        def operation1(a, b):
            # a < i, b >= i
            res = float('inf')
            for i in range(1,26):
                count = sum(a[j] for j in range(i))
                count += sum(b[j] for j in range(i, 26))
                
                res = min(res, count)
                
            return res
        
        def operation3(a, b):
            res = float('-inf')

            for i in range(26):
                res = max(res, a[i] + b[i])
            
            return len(A) + len(B) - res
        
        return min(operation1(countA, countB), operation1(countB, countA), operation3(countA, countB))
                
        