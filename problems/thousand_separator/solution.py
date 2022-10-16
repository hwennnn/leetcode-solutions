class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        ans = ""
        i = 0
        
        for s in reversed(str(n)):
            if i !=0 and i%3==0:
                ans += "."
            ans += s
            i+=1
        
        ans = ans[::-1]
        
        return ans