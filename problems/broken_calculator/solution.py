class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue == target: return 0
        if startValue > target: return startValue - target
        
        if target % 2 == 0:
            return self.brokenCalc(startValue, target // 2) + 1
        else:
            return self.brokenCalc(startValue, target + 1) + 1