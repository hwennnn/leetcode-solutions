# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        self.s = set()
        self.build(root)
        
    def find(self, target: int) -> bool:
        return target in self.s
    
    def build(self, root):
        if not root: return
        
        if root.left:
            root.left.val = root.val*2 + 1
            self.s.add(root.left.val)
            self.build(root.left)
        
        if root.right:
            root.right.val = root.val*2 + 2
            self.s.add(root.right.val)
            self.build(root.right)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)