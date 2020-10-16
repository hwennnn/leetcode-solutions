class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        
        c = collections.Counter(nums).items()

        for num,freq in c:
            buckets[freq].append(num)
            
        arr = list(chain(*buckets))
        
        return arr[::-1][:k]