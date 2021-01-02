class Solution:
    def maxLength(self, A: List[str]) -> int:
        dp = [set()]
        
        for a in A:
            if len(set(a)) < len(a): continue
            
            a = set(a)
            for b in dp[:]:
                if a & b: continue
                dp.append(a | b)
            
            
        return max(len(a) for a in dp)