class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        t = [[1], [1, 1]]
        
        for index in range(2, rowIndex + 1):
            tt = t[-1]
            tmp = [1] + [0] * (index - 1) + [1]
            for i in range(1, len(tmp) - 1):
                left = tt[i - 1]
                right = tt[-1] if i + 1 >= len(tt) else tt[i]
                tmp[i] = left + right
            
            t.append(tmp)
        
        return t[rowIndex]