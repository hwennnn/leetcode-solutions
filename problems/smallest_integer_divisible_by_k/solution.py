class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 and k % 5 == 0: return -1
        mod_set = set()
        prev = 0
        
        for i in range(1, k + 1):
            prev = (prev * 10 + 1) % k
            if prev == 0: return i
            if prev in mod_set: return -1
            mod_set.add(prev)
        
        return -1