class Solution:
    def digitCount(self, num: str) -> bool:
        count = Counter(num)
        
        for i, x in enumerate(num):
            if count[str(i)] != int(x):
                return False
        
        return True