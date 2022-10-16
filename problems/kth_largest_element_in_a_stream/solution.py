class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for x in nums:
            if len(self.heap) == k:
                heapq.heappushpop(self.heap, x)
            else:
                heapq.heappush(self.heap, x)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)