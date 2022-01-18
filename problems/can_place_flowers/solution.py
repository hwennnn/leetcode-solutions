class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], k: int) -> bool:
        n = len(flowerbed)
        put = i = 0
        
        while i < n:
            if flowerbed[i] == 1:
                i += 2
            else:
                if i == n - 1 or (i + 1 < n and flowerbed[i + 1] == 0):
                    put += 1
                    i += 2
                else:
                    i += 1
        
        return put >= k