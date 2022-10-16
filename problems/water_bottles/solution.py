class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles >= numExchange:
            remain = numBottles%numExchange
            numBottles //= numExchange
            res += numBottles
            numBottles += remain

        return res
           