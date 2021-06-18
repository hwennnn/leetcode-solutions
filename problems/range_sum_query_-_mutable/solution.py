class SegmentTree:
    
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        self.total = 0

class NumArray:

    def __init__(self, nums: List[int]):
        self.root = self.buildTree(nums, 0, len(nums) - 1)
    
    def buildTree(self, nums, start, end):
        if start > end: return None
        
        node = SegmentTree(start, end)
        
        if start == end:
            node.total = nums[start]
        else:
            mid = start + (end - start) // 2
            node.left = self.buildTree(nums, start, mid)
            node.right = self.buildTree(nums, mid + 1, end)
            node.total = node.left.total + node.right.total
        
        return node

    def update(self, index: int, val: int) -> None:
        self.updateR(self.root, index, val)
    
    def updateR(self, node, index, val):
        
        if node.start == node.end:
            node.total = val
        else:
            mid = node.start + (node.end - node.start) // 2
            if index <= mid:
                self.updateR(node.left, index, val)
            else:
                self.updateR(node.right, index, val)
            
            node.total = node.left.total + node.right.total

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeR(self.root, left, right)
    
    def sumRangeR(self, node, left, right):   
        if not node or node.start > right or node.end < left: return 0

        if node.start >= left and node.end <= right: return node.total
        
        l = self.sumRangeR(node.left, left, right)
        r = self.sumRangeR(node.right, left, right)
        
        return l + r


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)