class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            x = arr[i]
            for j in range(i+1, len(arr)):
                x ^= arr[j]
                if x == 0:
                    res += (j - i)
        
        return res