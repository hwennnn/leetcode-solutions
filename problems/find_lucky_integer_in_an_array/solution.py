class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lst = collections.Counter(arr)
        ans = -1
        for num in lst:
            if num == lst[num]:
                if num > ans:
                    ans = num

        return ans