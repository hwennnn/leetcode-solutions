# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.A = deque()
        
        dq = deque()
        if root:
            dq.append(root)
        
        while dq:
            node = dq.popleft()
            self.A.append(node)
            
            for child in (node.left, node.right):
                if child:
                    dq.append(child)

    def insert(self, val: int) -> int:
        while self.A and self.A[0].left and self.A[0].right:
            self.A.popleft()
        
        node = TreeNode(val)
        curr = self.A[0]
        
        if not curr.left:
            curr.left = node
        elif not curr.right:
            curr.right = node
            self.A.popleft()
        
        self.A.append(node)
        
        return curr.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()