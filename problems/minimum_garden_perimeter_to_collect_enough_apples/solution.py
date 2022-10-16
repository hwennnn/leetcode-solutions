class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        i = 1
        curr = 0
        
        while True:
            first = i + 1
            last = (i * 2) - 1
            
            temp = ((first + last) * (last - first + 1)) // 2
            temp *= 8
            
            temp += (i * 4) + (i * 2) * 4
            curr += temp
            
            if curr >= neededApples: break
            
            i += 1
            
        return i * 8 