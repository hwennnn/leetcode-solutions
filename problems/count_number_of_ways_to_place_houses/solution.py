class Solution:
    def countHousePlacements(self, n: int) -> int:
        houses = spaces = 1
        total = houses + spaces
        M = 10 ** 9 + 7
        
        for i in range(1, n):
            houses = spaces
            spaces = total
            total = (houses + spaces) % M
        
        return total * total % M
        