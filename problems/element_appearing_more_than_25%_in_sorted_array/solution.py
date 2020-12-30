class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        m = len(arr) // 4
        
        for i in range(n-m+1):
            if arr[i] == arr[i+m]:
                return arr[i]