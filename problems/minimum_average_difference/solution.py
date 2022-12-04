class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        left = 0
        right = sum(nums)
        minAverage = inf
        index = -1

        for i, x in enumerate(nums):
            left += x
            right -= x

            leftAverage = left // (i + 1)
            rightAverage = right // (N - i - 1) if i < N - 1 else 0
            average = abs(leftAverage - rightAverage)

            if average < minAverage:
                minAverage = average
                index = i
        
        return index