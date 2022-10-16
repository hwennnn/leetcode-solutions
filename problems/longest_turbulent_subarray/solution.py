class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        res = curr = 0

        for i in range(n):
            if i >= 2 and ((arr[i - 2] > arr[i - 1] < arr[i]) or (arr[i - 2] < arr[i - 1] > arr[i])):
                curr += 1
            elif i >= 1 and arr[i - 1] != arr[i]:
                curr = 2
            else:
                curr = 1
            
            res = max(res, curr)
        
        return res