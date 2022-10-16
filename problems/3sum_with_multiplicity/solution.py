class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n = len(arr)
        count = Counter()
        M = 10 ** 9 + 7
        res = 0
        
        for i in range(n):
            res = (res + count[target - arr[i]]) % M
            
            for j in range(i):
                m = arr[i] + arr[j]
                
                count[m] += 1
        
        return res
        