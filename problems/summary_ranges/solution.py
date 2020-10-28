class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        nums.append(float("inf"))
        res = []
        first = last = nums[0]
        
        for num in nums[1:]:
            if num - 1 != last:
                if first == last:
                    res.append(str(first))
                else:
                    res.append(f"{first}->{last}")
                first = num
                last = num
            
            else:
                last = num
        
        return res
                