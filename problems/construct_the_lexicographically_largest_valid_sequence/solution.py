class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (n*2 - 1)
        used = [0] * (n+1)
        
        def backtrack(i):
            if i == len(res): 
                return True
            
            if res[i]:
                return backtrack(i+1)
            
            for k in range(n, 1, -1):
                if used[k]: continue
                
                if i + k < len(res) and not res[i+k]:
                    res[i] = res[i+k] = k
                    used[k] = 1
                    
                    if backtrack(i+1): return True
                    
                    res[i] = res[i+k] = 0
                    used[k] = 0
            
            if not used[1]:
                res[i] = 1
                used[1] = 1
                
                if backtrack(i+1): return True
                
                res[i] = 0
                used[1] = 0
            
            
            return False
                
        
        backtrack(0)
        
        return res
        