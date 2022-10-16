class Solution:
    def sumGame(self, nums: str) -> bool:
        n = len(nums)
        half = n // 2
        left_sum = sum(int(c) for c in nums[:half] if c != '?')
        right_sum = sum(int(c) for c in nums[half:] if c != '?')
        left_count = nums[:half].count('?')
        right_count = nums[half:].count('?')
        
        def canAliceWin(left_sum, right_sum, left_count, right_count):
            for i in range(left_count + right_count):
                if i % 2 == 0:
                    if left_count > 0:
                        left_sum += 9
                        left_count -= 1
                    else:
                        right_count -= 1
                else:
                    if right_count > 0:
                        right_sum += 9
                        right_count -= 1
                    else:
                        left_count -= 1
                
            return left_sum != right_sum
        
        return canAliceWin(left_sum, right_sum, left_count, right_count) or canAliceWin(right_sum, left_sum, right_count, left_count)