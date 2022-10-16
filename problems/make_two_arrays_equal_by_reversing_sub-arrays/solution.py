class Solution:
    def canBeEqual(self, target: List[int], lst: List[int]) -> bool:
        
        n = 1001
        arr = [0]*n
        
        for i in range(len(target)):
            arr[target[i]] += 1
            arr[lst[i]] -= 1
        
        for i in range(n):   
            if arr[i] != 0:
                return False
        
        return True
        
        