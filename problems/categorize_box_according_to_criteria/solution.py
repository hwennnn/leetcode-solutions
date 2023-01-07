class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        dimensions = [length, width, height, mass]
        
        isBulky = any(d >= 10 ** 4 for d in dimensions) or length * width * height >= 10 ** 9
        isHeavy = mass >= 100
        
        if isBulky and isHeavy:
            return "Both"
        elif not isBulky and not isHeavy:
            return "Neither"
        elif isBulky:
            return "Bulky"
        elif isHeavy:
            return "Heavy"