class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0
        toFill = []

        for cap, rock in zip(capacity, rocks):
            if rock < cap:
                toFill.append(cap - rock)
            else:
                res += 1
        
        toFill.sort()

        for rock in toFill:
            if additionalRocks >= rock:
                res += 1
                additionalRocks -= rock
            else:
                break

        return res