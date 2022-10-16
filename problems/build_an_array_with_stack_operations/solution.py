class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = [i for i in range(1,n+1)]
        res = []
        j = 0
        for i in range(n):
            if j >= len(target):
                break
            if arr[i] != target[j]:
                res.append("Push")
                res.append("Pop")
            else:
                res.append("Push")
                j += 1
        return res