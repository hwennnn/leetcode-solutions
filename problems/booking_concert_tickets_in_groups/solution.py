class Node:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        self.total = 0
        self.mx = 0

class SegTree:

    def __init__(self, n, val):
        self.root = self.buildTree(0, n, val)
    
    def buildTree(self, start, end, val):
        if start > end: return None

        if start == end:
            node = Node(start, end)
            node.total = val
            node.mx = val
            
            return node
        
        node = Node(start, end)
        mid = start + (end - start) // 2
        node.left = self.buildTree(start, mid, val)
        node.right = self.buildTree(mid + 1, end, val)
        node.total = node.left.total + node.right.total
        node.mx = max(node.left.mx, node.right.mx)
        
        return node

    def update(self, index: int, val: int) -> None:
        self.updateR(self.root, index, val)
    
    def updateR(self, node, index, val):
        
        if node.start == node.end:
            node.total -= val
            node.mx -= val
        else:
            mid = node.start + (node.end - node.start) // 2
            if index <= mid:
                self.updateR(node.left, index, val)
            else:
                self.updateR(node.right, index, val)
            
            node.total = node.left.total + node.right.total
            node.mx = max(node.left.mx, node.right.mx)

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeR(self.root, left, right)
    
    def sumRangeR(self, node, left, right):   
        if not node or node.start > right or node.end < left: return 0

        if node.start >= left and node.end <= right: return node.total
        
        l = self.sumRangeR(node.left, left, right)
        r = self.sumRangeR(node.right, left, right)
        
        return l + r
    
    def maxQuery(self, k, maxRow, seats):
        
        def maxQueryHelper(node):
            if node.start == node.end:
                if node.end > maxRow or node.total < k:
                    return []
                
                if node.end <= maxRow and node.total >= k:
                    return [node.end, seats - node.total]
        
            return maxQueryHelper(node.left) if node.left.mx >= k else maxQueryHelper(node.right)
        
        return maxQueryHelper(self.root)
        
class BookMyShow:

    def __init__(self, n: int, m: int):
        self.seg = SegTree(n - 1, m)  
        self.seats = [m] * n
        self.m = m
        self.n = n
        self.startRow = 0
        
    def gather(self, k: int, maxRow: int) -> List[int]:
        res = self.seg.maxQuery(k, maxRow, self.m)
        
        if res:
            row = res[0]
            self.seg.update(row, k)
            self.seats[row] -= k
        
        return res
        

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.seg.sumRange(0, maxRow) < k:
            return False
    
        index = self.startRow
        curr = 0
        
        while curr < k:
            rest = k - curr
            
            if rest >= self.seats[index]:
                self.seg.update(index, self.seats[index])
                curr += self.seats[index]
                self.seats[index] = 0
                index += 1
                self.startRow = index
            else:
                self.seg.update(index, rest)
                self.seats[index] -= rest
                curr += rest
        
        return True
        
# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)