class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k: return arr
        
        i = bisect.bisect_left(arr, x) - 1
        j = i + 1
        
        while j - i - 1 < k:
            if i == -1:
                j += 1
                continue
            
            if j == len(arr) or abs(arr[i] - x) <= abs(arr[j] - x):
                i -= 1
            else:
                j += 1
            
        return arr[i + 1: j]