class Solution:
    def addDigits(self, num: int) -> int:
        
        return num % 9 if num % 9 else 9 if num else 0