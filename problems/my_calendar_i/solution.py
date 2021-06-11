class BST:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
class MyCalendar:

    def __init__(self):
        self.root = None
    
    def bookHelper(self, start, end, node):
        if start >= node.end:
            if node.right:
                return self.bookHelper(start, end, node.right)
            else:
                node.right = BST(start, end)
                return True
        elif end <= node.start:
            if node.left:
                return self.bookHelper(start, end, node.left)
            else:
                node.left = BST(start, end)
                return True
        
        return False
        

    def book(self, start: int, end: int) -> bool:
        
        if not self.root:
            self.root = BST(start, end)
            return True
        
        return self.bookHelper(start, end, self.root)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)