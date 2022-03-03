class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort()
        diff = arr[1] - arr[0]
        
        for i in range(2, n):
            d = arr[i] - arr[i - 1]
            if d != diff: return False
        
        return True