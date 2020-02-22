# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root == None:
            return None
        
        while (root and root.val != val):
            if root.val > val:
                root = self.searchBST(root.left,val)
            
            else:
                root = self.searchBST(root.right,val)
                
        return root