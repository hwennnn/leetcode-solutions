class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0: return [0] * n
        res = []
        
        for i,x in enumerate(code):
            num = 0
            for _ in range(abs(k)):
                if k < 0:
                    i = (i-1)%n
                else:
                    i = (i+1)%n
                num += code[i]
            
            res.append(num)
        
        return res