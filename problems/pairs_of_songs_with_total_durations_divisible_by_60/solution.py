class Solution:
    def numPairsDivisibleBy60(self, arr: List[int]) -> int:
        
        res = 0
        n = len(arr)
        dic = [0] * 60
        
        for i in range(n):
            target = (60 - arr[i]%60)%60
            res += dic[target]
            dic[arr[i]%60] += 1
               
        return res
        