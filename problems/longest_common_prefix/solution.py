class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        w = min(strs, key = len)
        res = ""
        
        for i, x in enumerate(w):
            flag = True
            
            for word in strs:
                if word[i] != x:
                    flag = False
                    break
            
            if flag:
                res += x
            else:
                break
        
        return res