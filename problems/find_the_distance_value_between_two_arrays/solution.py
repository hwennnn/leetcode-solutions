class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for a1 in arr1:
            if all(abs(a1-a2) > d for a2 in arr2):
                count += 1

        return count