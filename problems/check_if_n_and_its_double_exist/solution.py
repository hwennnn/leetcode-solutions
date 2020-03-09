class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        check = set()
        
        for num in arr:
            if num * 2 in check or (num % 2 == 0 and num // 2 in check):
                return True
            
            check.add(num)
            
        return False