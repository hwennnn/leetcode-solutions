class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        i, j = 0, n-1
        
        while j - i >= k:
            if abs(arr[i]- x) <= abs(arr[j] - x):
                j -= 1
            else:
                i += 1
                
        
        return arr[i:j+1]