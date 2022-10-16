class Solution:
    def minimumDeletions(self, s: str) -> int:
        c = collections.Counter(s)
        
        a_right = c["a"]
        b_right = c["b"]
        
        a_left = b_left = 0
        res = len(s)
        
        for c in s+"b":

            res = min(res, b_left + a_right)
                
            if c == "a":
                a_left += 1
                a_right -= 1
            else:
                b_left += 1
                b_right -= 1
            
            
        
        return res
            