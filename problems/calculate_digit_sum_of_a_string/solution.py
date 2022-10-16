class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            i = 0
            n = len(s)
            curr = 0
            temp = []
            count = 0
            
            while i < n:
                count += 1
                curr += int(s[i])
                
                if count == k or i == n - 1:
                    temp.append(str(curr))        
                    curr = 0
                    count = 0
                    
                i += 1
            
            s = "".join(temp)
        
        return s