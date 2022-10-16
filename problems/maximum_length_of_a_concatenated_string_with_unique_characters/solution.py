class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        
        for a in arr:
            if len(set(a)) < len(a): continue
            
            a = set(a)
            for b in dp[:]:
                if a & b: continue
                dp.append(a | b)
        
        return max(len(x) for x in dp)