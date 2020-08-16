class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        n = len(strs)
        if (n <= 0):
            return ""
        
        lens = [len(i) for i in strs]
        min_len = min(lens)
        result = ""
        
        for i in range(1, min_len+1):
            prefix = strs[0][:i]
            
            for s in strs:
                if s[:i] != prefix:
                    return result
                
            result = prefix
        
        return result
                