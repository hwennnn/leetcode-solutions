class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix = [0]
        for x in range(1, n + 1):
            prefix.append(prefix[-1] + x)
        
        for i in range(1, n + 1):
            if prefix[i - 1] == prefix[-1] - prefix[i]:
                return i
        
        return -1