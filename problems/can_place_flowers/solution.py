class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        plots = [0] + flowerbed + [0]
        
        i = 1
        
        while i<= len(flowerbed) and n>0:
            if plots[i] == 0 and plots[i-1] == 0 and plots[i+1] == 0:
                plots[i] = 1
                n-=1
            
            i += 1
            
        return n == 0