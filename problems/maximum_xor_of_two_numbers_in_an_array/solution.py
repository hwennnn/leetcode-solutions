class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = res = 0
        
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            
            sset = set()
            for num in nums:
                sset.add(num & mask)
            
            desired = res | (1 << i)
            for prefix in sset:
                anotherSum = prefix ^ desired
                
                if anotherSum in sset:
                    res = desired
                    break
            
        return res