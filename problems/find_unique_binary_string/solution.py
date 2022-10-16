class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""
        
        for i, x in enumerate(nums):
            res += "0" if x[i] == "1" else "1"
        
        return res