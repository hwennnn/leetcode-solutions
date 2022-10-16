class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""

        for key, group in itertools.groupby(num):
            if len(list(group)) >= 3:
                res = max(res, key * 3)

        return res
                