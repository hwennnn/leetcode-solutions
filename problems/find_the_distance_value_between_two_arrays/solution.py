class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        n1, n2 = len(arr1), len(arr2)
        ans = 0
        
        for i in range(n1):
            check = True
            for j in range(n2):
                if abs(arr1[i] - arr2[j]) <= d:
                    check = False
                    break
            
            ans += check
            
        return ans