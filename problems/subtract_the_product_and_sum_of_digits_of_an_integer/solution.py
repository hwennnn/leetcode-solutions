class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        lst = [int(i) for i in str(n)]
        prod = 1
        for i in lst:
            prod *= i
        
        return prod - sum(lst)