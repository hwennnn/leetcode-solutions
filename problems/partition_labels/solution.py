class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        
        for index, char in enumerate(s):
            mp[char] = index
        
        maxIndex = float('-inf')
        lastIndex = 0
        res = []
        
        for index, char in enumerate(s):
            maxIndex = max(maxIndex, mp[char])
            
            if index == maxIndex:
                res.append(maxIndex - lastIndex + 1)
                lastIndex = index + 1
        
        return res