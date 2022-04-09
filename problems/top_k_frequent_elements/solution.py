class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        
        c = collections.Counter(nums).items()

        for num,freq in c:
            buckets[freq].append(num)
            
        res = []
        pointer = len(buckets) - 1
        
        while k > 0 and pointer >= 0:
            while k > 0 and len(buckets[pointer]) > 0:
                res.append(buckets[pointer].pop())
                k -= 1
            pointer -= 1
            
        return res