class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows = len(bank)
        prev = bank[0].count("1")
        res = 0
        
        for i in range(1, rows):
            curr = bank[i].count("1")
            
            if curr == 0: continue
                
            res += prev * curr
            
            prev = curr
        
        return res