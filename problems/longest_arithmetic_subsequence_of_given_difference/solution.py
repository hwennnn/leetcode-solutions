class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mp = collections.defaultdict(int)
        
        for num in arr:
            mp[num] = 1 if num - difference not in mp else mp[num-difference] + 1
        
        return max(mp.values())