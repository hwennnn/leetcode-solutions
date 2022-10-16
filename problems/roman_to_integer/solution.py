class Solution:
    def romanToInt(self, s: str):
        
        mp = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = 0
        total = 0
        
        for i in s[::-1]:
            curr = mp[i]
            if prev > curr:
                total -= curr
            else:
                total += curr
            prev = curr
            
        return total