class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i != j:
                    if arr[i] == 2*arr[j]:
                        return True
        
        return False