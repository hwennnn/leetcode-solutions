class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        res = []
        
        for index, num in enumerate(nums):
            s = str(num)
            curr = ""
            
            for char in s:
                curr += str(mapping[int(char)])
            
            res.append((int(curr), index, num))
        
        return [num for _, __, num in sorted(res)]