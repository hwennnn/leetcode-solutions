class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        res = 0
        
        for i in range(n-m):
            
            if arr[i] != arr[i+m]:
                res = 0
                
            res += (arr[i] == arr[i+m])
            
            if res == (k-1)*m:
                return True
        
        return False
            