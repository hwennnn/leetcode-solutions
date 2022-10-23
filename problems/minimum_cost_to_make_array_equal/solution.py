class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        N = len(nums)
        A = sorted((x, c) for x, c in zip(nums, cost))
        nums = [a for a, _ in A]
        cost = [b for _, b in A]
        
        prefix = [0]
        curr = cost[0]
        for i in range(1, N):
            prefix.append(prefix[-1] + (nums[i] - nums[i - 1]) * curr)
            curr += cost[i]
        
        suffix = [0]
        curr = cost[-1]
        for i in range(N - 2, -1, -1):
            suffix.append(suffix[-1] + (nums[i + 1] - nums[i]) * curr)
            curr += cost[i]
        suffix.reverse()
        
        return min(prefix[i] + suffix[i] for i in range(N))