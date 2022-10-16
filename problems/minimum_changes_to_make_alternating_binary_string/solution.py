class Solution:
    def minOperations(self, s: str) -> int:
        
        n = len(s)
        
        first, second = ["1"], ["0"]
        
        for _ in range(n-1):
            first.append(second[-1])
            second.append(first[-2])
        
        def diff(word):
            return sum(a != b for a,b in zip(word, s))
        
        return min(diff(first), diff(second))
            