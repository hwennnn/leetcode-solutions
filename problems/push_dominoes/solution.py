class Solution:
    def pushDominoes(self, d: str) -> str:
        d = 'L' + d + 'R'
        res = ''
        i = 0
        
        for j in range(1, len(d)):
            if d[j] == '.': continue
            
            middle = j - i - 1
            if i > 0:
                res += d[i]
            
            if d[i] == d[j]:
                res += d[j] * middle
            elif d[i] == 'L' and d[j] == 'R':
                res += '.' * middle
            else:
                res += 'R' * (middle // 2) + '.' * (middle % 2) + 'L' * (middle // 2)
            
            i = j
        
        return res