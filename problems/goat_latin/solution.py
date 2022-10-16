class Solution:
    def toGoatLatin(self, S: str) -> str:
    
        vowel = {"a","e","i","o","u"}
        words = S.split(" ")
        i = 1
        ans = []
        for word in words:
            a = ""
            
            if word[0].lower() in vowel:
                a = word + "ma"
            else:
                a = word[1:] + word[0] + "ma"
            
            a += "a"*i
            i+=1
        
            ans.append(a)
        
        return " ".join(ans)
                