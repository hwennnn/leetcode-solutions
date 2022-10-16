class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        n = len(brackets)
        first = min(brackets[0][0], income)
        res =  first * (brackets[0][1] / 100)
        income -= first
        
        for i in range(1, n):
            k = brackets[i][0] - brackets[i - 1][0]
            curr = min(income, k)
            income -= curr
            res += curr * (brackets[i][1] / 100)
            
            if income == 0:
                break
        
        return res