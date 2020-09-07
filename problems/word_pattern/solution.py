class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        S = s.split()
        dic = {}
        
        if len(S) != len(pattern): return False
        
        for i in range(len(S)):
            if S[i] not in dic:
                if pattern[i] in dic.values():
                    return False
                dic[S[i]] = pattern[i]
        
        for i in range(len(S)):
            if pattern[i] != dic[S[i]]:
                return False
        
        return True
            