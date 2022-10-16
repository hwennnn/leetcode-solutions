class Solution:
    def isPrefixOfWord(self, sentence: str, sw: str) -> int:
        S = sentence.split()
        
        l = 0
        for s in S:
            l += 1
            if len(sw) > len(s): continue
            check = True
            for i in range(min(len(s), len(sw))):
                if sw[i] != s[i]:
                    check = False
                    break
            
            if check:
                return l
            
        
        return -1