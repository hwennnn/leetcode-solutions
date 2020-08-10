class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def helper(s):
            
            temp = list(s)
            new = []
            
            for i in reversed(range(len(temp))):
                if temp[i] == "0":
                    new.append("1")
                else:
                    new.append("0")
                    
                
            return "".join(new)
    
            
            
            return s
        
        
        s = "0"
        
        for i in range(1,n):
            s = s + "1" + helper(s)

        
        
        return s[k-1]
            