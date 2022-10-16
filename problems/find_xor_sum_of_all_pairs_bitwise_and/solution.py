class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xora = xorb = 0
        
        for num in arr1:
            xora ^= num
        
        for num in arr2:
            xorb ^= num
        
        return xora & xorb