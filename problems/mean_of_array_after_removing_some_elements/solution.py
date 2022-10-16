class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        k = int(len(arr)*0.05)
        
        arr.sort()
        count = res = 0
        
        for i in range(k,n-k):
            res += 1
            count += arr[i]
        
        return count / res
            